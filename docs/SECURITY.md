# Security and Compliance Guide

## Overview

The Contentious Estates system implements comprehensive security and audit logging to ensure compliance with legal and regulatory requirements for contentious probate case management.

## Security Features

### 1. Audit Logging

All operations on case data are automatically logged with:
- Timestamp (UTC timezone-aware)
- Event type
- User ID
- Case ID
- Operation details
- Metadata

**Example Audit Log Entry:**
```json
{
  "timestamp": "2025-11-16T20:45:31.380888+00:00",
  "event_type": "STORE_DATE",
  "user_id": "case_manager_001",
  "case_id": "PROB_2025_001",
  "details": "Stored date: filing_deadline = 2025-12-31",
  "metadata": {}
}
```

### 2. Access Control

The system supports user-specific memory filtering:

```python
memory = ContentiousProbateMemory(
    user_id="user_123",
    case_id="case_456"
)
```

Each memory instance is isolated by user and case ID, preventing cross-case data access.

### 3. Secure Trace Logging

Runtime operations are logged securely without exposing sensitive data:

```python
from contentious_estates.audit_logger import SecureTraceLogger

trace = SecureTraceLogger()
trace.trace("Operation started", operation="case_update")
```

### 4. Data Encryption (Future Enhancement)

Configuration supports encryption settings:

```bash
ENABLE_ENCRYPTION=true
SECRET_KEY=your-secure-key-here
```

## Compliance

### Data Retention

Audit logs are persisted to disk and can be:
- Archived for compliance requirements
- Analyzed for security audits
- Used for forensic investigation

### GDPR Compliance Considerations

For GDPR compliance:

1. **Data Minimization**: Store only necessary case information
2. **Right to Access**: Use `get_case_context()` to provide data exports
3. **Right to Erasure**: Implement case deletion workflows
4. **Audit Trail**: All access and modifications are logged

### Legal Hold

Audit logs provide:
- Complete history of case modifications
- User attribution for all changes
- Timestamp evidence for legal proceedings

## Best Practices

### 1. Enable Audit Logging

Always enable audit logging in production:

```python
memory = ContentiousProbateMemory(
    user_id="user_id",
    case_id="case_id",
    enable_audit=True  # Always True in production
)
```

### 2. Secure Audit Log Storage

Protect audit log files:

```bash
# Set restrictive permissions
chmod 600 audit.log

# Regular backups
cp audit.log /secure/backup/location/

# Rotate logs regularly
logrotate /etc/logrotate.d/contentious_estates
```

### 3. Regular Security Audits

Review audit logs regularly:

```python
import json

with open('audit.log', 'r') as f:
    for line in f:
        if 'AUDIT' in line:
            # Extract JSON from log line
            log_data = json.loads(line.split('- INFO - ')[1])
            
            # Check for suspicious activity
            if log_data['event_type'].startswith('SECURITY_'):
                print(f"Security event: {log_data}")
```

### 4. User Authentication

Integrate with your authentication system:

```python
def get_authenticated_memory(request, case_id):
    """Get memory instance for authenticated user"""
    user_id = request.user.id  # From your auth system
    
    # Verify user has access to case
    if not user_has_access(user_id, case_id):
        audit.log_security_event(
            "UNAUTHORIZED_ACCESS",
            user_id=user_id,
            case_id=case_id,
            severity="WARNING"
        )
        raise PermissionError("Access denied")
    
    return ContentiousProbateMemory(
        user_id=user_id,
        case_id=case_id
    )
```

### 5. Sensitive Data Handling

For sensitive information:

```python
# Don't store actual sensitive data in descriptions
memory.store_evidence(
    file_name="medical_records.pdf",
    description="Medical records (encrypted)",
    metadata={
        "encrypted": True,
        "encryption_key_id": "key_123",
        "storage_location": "secure/vault/path"
    }
)
```

## Monitoring

### Real-time Monitoring

Monitor audit logs in real-time:

```bash
tail -f audit.log | grep SECURITY_
```

### Alerting

Set up alerts for security events:

```python
import re

def monitor_audit_log(log_file):
    """Monitor audit log for security events"""
    with open(log_file, 'r') as f:
        f.seek(0, 2)  # Go to end
        while True:
            line = f.readline()
            if 'SECURITY_' in line:
                send_alert(line)
            time.sleep(1)
```

## Incident Response

### 1. Identify

Check audit logs for the incident timeframe:

```python
def find_incidents(start_time, end_time):
    """Find all events in timeframe"""
    events = []
    with open('audit.log', 'r') as f:
        for line in f:
            if 'AUDIT' in line:
                data = json.loads(line.split('- INFO - ')[1])
                timestamp = datetime.fromisoformat(data['timestamp'])
                if start_time <= timestamp <= end_time:
                    events.append(data)
    return events
```

### 2. Investigate

Review all operations by affected user/case:

```python
def get_user_activity(user_id):
    """Get all activity for a user"""
    activity = []
    with open('audit.log', 'r') as f:
        for line in f:
            if user_id in line:
                data = json.loads(line.split('- INFO - ')[1])
                activity.append(data)
    return activity
```

### 3. Remediate

Take appropriate action based on findings.

### 4. Document

Audit logs provide complete documentation of the incident.

## Regular Maintenance

### Log Rotation

Configure log rotation to prevent disk space issues:

```bash
# /etc/logrotate.d/contentious_estates
/path/to/audit.log {
    daily
    rotate 365
    compress
    delaycompress
    notifempty
    create 0600 app app
    sharedscripts
}
```

### Backup Strategy

Implement regular backups:

```bash
#!/bin/bash
# backup-audit-logs.sh

DATE=$(date +%Y%m%d)
BACKUP_DIR=/secure/backups/audit-logs
SOURCE=/path/to/audit.log

cp $SOURCE $BACKUP_DIR/audit-$DATE.log
gzip $BACKUP_DIR/audit-$DATE.log
```

## Reporting

### Generate Compliance Reports

```python
def generate_compliance_report(start_date, end_date):
    """Generate compliance report for date range"""
    
    events_by_type = {}
    events_by_user = {}
    
    with open('audit.log', 'r') as f:
        for line in f:
            if 'AUDIT' in line:
                data = json.loads(line.split('- INFO - ')[1])
                timestamp = datetime.fromisoformat(data['timestamp'])
                
                if start_date <= timestamp <= end_date:
                    # Count by type
                    event_type = data['event_type']
                    events_by_type[event_type] = events_by_type.get(event_type, 0) + 1
                    
                    # Count by user
                    user_id = data['user_id']
                    events_by_user[user_id] = events_by_user.get(user_id, 0) + 1
    
    return {
        'period': f"{start_date} to {end_date}",
        'events_by_type': events_by_type,
        'events_by_user': events_by_user,
        'total_events': sum(events_by_type.values())
    }
```

## Additional Resources

- [GDPR Compliance Checklist](https://gdpr.eu/checklist/)
- [OWASP Security Guidelines](https://owasp.org/)
- [Data Protection Best Practices](https://ico.org.uk/for-organisations/)
