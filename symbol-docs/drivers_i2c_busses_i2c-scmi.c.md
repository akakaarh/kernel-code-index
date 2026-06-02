# drivers/i2c/busses/i2c-scmi.c

Subsystem: drivers/i2c

## Functions (6)

### acpi_smbus_cmi_access
- Return type: static int
- Signature: acpi_smbus_cmi_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 74

### acpi_smbus_cmi_add_cap
- Return type: static int
- Signature: acpi_smbus_cmi_add_cap(struct acpi_smbus_cmi * smbus_cmi,const char * name)
- Line: 293

### acpi_smbus_cmi_func
- Return type: static u32
- Signature: acpi_smbus_cmi_func(struct i2c_adapter * adapter)
- Line: 264

### acpi_smbus_cmi_query_methods
- Return type: static acpi_status
- Signature: acpi_smbus_cmi_query_methods(acpi_handle handle,u32 level,void * context,void ** return_value)
- Line: 340

### smbus_cmi_probe
- Return type: static int
- Signature: smbus_cmi_probe(struct platform_device * device)
- Line: 356

### smbus_cmi_remove
- Return type: static void
- Signature: smbus_cmi_remove(struct platform_device * device)
- Line: 404

## Structs (2)

### acpi_smbus_cmi
- Line: 22
- Members:
  - mt_info: char *
  - mt_sbr: char *
  - mt_sbw: char *
  - handle: acpi_handle
  - adapter: i2c_adapter
  - cap_info: u8:1
  - cap_read: u8:1
  - cap_write: u8:1
  - methods: const struct smbus_methods_t *

### smbus_methods_t
- Line: 16
- Members:
  - mt_info: char *
  - mt_sbr: char *
  - mt_sbw: char *
  - handle: acpi_handle
  - adapter: i2c_adapter
  - cap_info: u8:1
  - cap_read: u8:1
  - cap_write: u8:1
  - methods: const struct smbus_methods_t *

## Variables (5)

- static **acpi_smbus_cmi_algorithm** : const struct i2c_algorithm (line 287)
- static **acpi_smbus_cmi_ids** : const struct acpi_device_id[] (line 44)
- static **ibm_smbus_methods** : const struct smbus_methods_t (line 38)
- static **smbus_cmi_driver** : platform_driver (line 412)
- static **smbus_methods** : const struct smbus_methods_t (line 31)

## Macros (18)

- **ACPI_SMBUS_PRTCL_BLOCK_DATA** (line 70)
- **ACPI_SMBUS_PRTCL_BYTE** (line 67)
- **ACPI_SMBUS_PRTCL_BYTE_DATA** (line 68)
- **ACPI_SMBUS_PRTCL_QUICK** (line 66)
- **ACPI_SMBUS_PRTCL_READ** (line 65)
- **ACPI_SMBUS_PRTCL_WORD_DATA** (line 69)
- **ACPI_SMBUS_PRTCL_WRITE** (line 64)
- **ACPI_SMBUS_STATUS_ACC_DENY** (line 58)
- **ACPI_SMBUS_STATUS_BUSY** (line 61)
- **ACPI_SMBUS_STATUS_CMD_DENY** (line 56)
- **ACPI_SMBUS_STATUS_DERR** (line 55)
- **ACPI_SMBUS_STATUS_DNAK** (line 54)
- **ACPI_SMBUS_STATUS_FAIL** (line 53)
- **ACPI_SMBUS_STATUS_NOTSUP** (line 60)
- **ACPI_SMBUS_STATUS_OK** (line 52)
- **ACPI_SMBUS_STATUS_PEC** (line 62)
- **ACPI_SMBUS_STATUS_TIMEOUT** (line 59)
- **ACPI_SMBUS_STATUS_UNKNOWN** (line 57)
