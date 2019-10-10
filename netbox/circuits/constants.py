# Circuit statuses
CIRCUIT_STATUS_DEPROVISIONING = 0
CIRCUIT_STATUS_ACTIVE = 1
CIRCUIT_STATUS_PLANNED = 2
CIRCUIT_STATUS_PROVISIONING = 3
CIRCUIT_STATUS_OFFLINE = 4
CIRCUIT_STATUS_DECOMMISSIONED = 5
CIRCUIT_STATUS_CHOICES = [
    [CIRCUIT_STATUS_PLANNED, 'Planned'],
    [CIRCUIT_STATUS_PROVISIONING, 'Provisioning'],
    [CIRCUIT_STATUS_ACTIVE, 'Active'],
    [CIRCUIT_STATUS_OFFLINE, 'Offline'],
    [CIRCUIT_STATUS_DEPROVISIONING, 'Deprovisioning'],
    [CIRCUIT_STATUS_DECOMMISSIONED, 'Decommissioned'],
]

# CircuitTermination sides
TERM_SIDE_A = 'A'
TERM_SIDE_Z = 'Z'
TERM_SIDE_CHOICES = (
    (TERM_SIDE_A, 'A'),
    (TERM_SIDE_Z, 'Z'),
)
