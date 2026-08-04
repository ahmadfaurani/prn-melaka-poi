#!/bin/bash
# PRN Melaka POI Workstream — Git Sync Script
# Script-only cronjob (CJ-MLK-06)
# Auto-commits and pushes intelligence outputs to GitHub
# No tokens embedded — uses git credential.helper store

set -e

WORKDIR="/home/p62operator/.openclaw/workspace-mlk"
REPO="https://github.com/ahmadfaurani/prn-melaka-poi.git"

cd "$WORKDIR" || exit 1

# Initialize git if not already
if [ ! -d ".git" ]; then
    git init
    git remote add origin "$REPO"
    git branch -M main
fi

# Export cronjob configs for this workstream
python3 -c "
import json, subprocess, os

# Read cronjob configs
result = subprocess.run(['cat', os.path.expanduser('~/.hermes/cron/jobs.json')], capture_output=True, text=True)
jobs = json.loads(result.stdout)

# Filter Melaka-related cronjobs
mlk_jobs = []
for job in jobs:
    name = job.get('name', '')
    if 'Melaka' in name or 'MLK' in name or 'melaka' in name:
        mlk_jobs.append({
            'id': job.get('id'),
            'name': name,
            'schedule': job.get('schedule'),
            'deliver': job.get('deliver'),
            'enabled': job.get('enabled'),
            'workdir': job.get('workdir')
        })

config = {
    'workstream': 'PRN Melaka POI Intelligence',
    'exported_at': __import__('datetime').datetime.utcnow().isoformat() + 'Z',
    'repo': 'ahmadfaurani/prn-melaka-poi',
    'workspace': '/home/p62operator/.openclaw/workspace-mlk',
    'total_cronjobs': len(mlk_jobs),
    'cronjobs': mlk_jobs
}

with open(os.path.join('$WORKDIR', '05-TOOLS-AND-AUTOMATION/cronjob-configs.json'), 'w') as f:
    json.dump(config, f, indent=2)
print(f'Exported {len(mlk_jobs)} cronjobs to cronjob-configs.json')
"

# Stage all changes
git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No changes to commit. Sync complete."
    exit 0
fi

# Commit and push
TIMESTAMP=$(TZ=Asia/Kuala_Lumpur date '+%Y-%m-%d %H:%M %Z')
git commit -m "Auto-sync: PRN Melaka POI intelligence update — $TIMESTAMP"

# Push (credential.helper store handles auth)
git push -u origin main 2>/dev/null || git push origin main 2>/dev/null || echo "Push failed — will retry next cycle"

echo "Git sync complete: $TIMESTAMP"
