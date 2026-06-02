# drivers/i2c/busses/i2c-amd-mp2-plat.c

Subsystem: drivers/i2c

## Functions (14)

### i2c_amd_check_cmd_completion
- Return type: static int
- Signature: i2c_amd_check_cmd_completion(struct amd_i2c_dev * i2c_dev)
- Line: 97

### i2c_amd_cmd_completion
- Return type: static void
- Signature: i2c_amd_cmd_completion(struct amd_i2c_common * i2c_common)
- Line: 85

### i2c_amd_dma_map
- Return type: static int
- Signature: i2c_amd_dma_map(struct amd_i2c_common * i2c_common)
- Line: 41

### i2c_amd_dma_unmap
- Return type: static void
- Signature: i2c_amd_dma_unmap(struct amd_i2c_common * i2c_common)
- Line: 64

### i2c_amd_enable_set
- Return type: static int
- Signature: i2c_amd_enable_set(struct amd_i2c_dev * i2c_dev,bool enable)
- Line: 123

### i2c_amd_func
- Return type: static u32
- Signature: i2c_amd_func(struct i2c_adapter * a)
- Line: 176

### i2c_amd_get_bus_speed
- Return type: static speed_enum
- Signature: i2c_amd_get_bus_speed(struct platform_device * pdev)
- Line: 211

### i2c_amd_probe
- Return type: static int
- Signature: i2c_amd_probe(struct platform_device * pdev)
- Line: 245

### i2c_amd_remove
- Return type: static void
- Signature: i2c_amd_remove(struct platform_device * pdev)
- Line: 325

### i2c_amd_resume
- Return type: static int
- Signature: i2c_amd_resume(struct amd_i2c_common * i2c_common)
- Line: 195

### i2c_amd_start_cmd
- Return type: static void
- Signature: i2c_amd_start_cmd(struct amd_i2c_dev * i2c_dev)
- Line: 77

### i2c_amd_suspend
- Return type: static int
- Signature: i2c_amd_suspend(struct amd_i2c_common * i2c_common)
- Line: 187

### i2c_amd_xfer
- Return type: static int
- Signature: i2c_amd_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 152

### i2c_amd_xfer_msg
- Return type: static int
- Signature: i2c_amd_xfer_msg(struct amd_i2c_dev * i2c_dev,struct i2c_msg * pmsg)
- Line: 133

## Structs (1)

### amd_i2c_dev
- Line: 31
- Members:
  - common: amd_i2c_common
  - pdev: platform_device *
  - adap: i2c_adapter
  - cmd_complete: completion

## Variables (5)

- static **amd_i2c_dev_quirks** : const struct i2c_adapter_quirks (line 240)
- static **i2c_amd_acpi_match** : const struct acpi_device_id[] (line 341)
- static **i2c_amd_algorithm** : const struct i2c_algorithm (line 181)
- static **i2c_amd_plat_driver** : platform_driver (line 347)
- static **supported_speeds** : const u32[] (line 203)

## Macros (3)

- **AMD_I2C_TIMEOUT** (line 22)
- **AMD_MP2_I2C_MAX_RW_LENGTH** (line 21)
- **amd_i2c_dev_common**(__common) (line 38)
