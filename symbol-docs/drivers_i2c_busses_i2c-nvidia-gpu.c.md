# drivers/i2c/busses/i2c-nvidia-gpu.c

Subsystem: drivers/i2c

## Functions (11)

### gpu_enable_i2c_bus
- Return type: static void
- Signature: gpu_enable_i2c_bus(struct gpu_i2c_dev * i2cd)
- Line: 61

### gpu_i2c_check_status
- Return type: static int
- Signature: gpu_i2c_check_status(struct gpu_i2c_dev * i2cd)
- Line: 80

### gpu_i2c_functionality
- Return type: static u32
- Signature: gpu_i2c_functionality(struct i2c_adapter * adap)
- Line: 229

### gpu_i2c_probe
- Return type: static int
- Signature: gpu_i2c_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 272

### gpu_i2c_read
- Return type: static int
- Signature: gpu_i2c_read(struct gpu_i2c_dev * i2cd,u8 * data,u16 len)
- Line: 108

### gpu_i2c_remove
- Return type: static void
- Signature: gpu_i2c_remove(struct pci_dev * pdev)
- Line: 332

### gpu_i2c_resume
- Return type: static __maybe_unused int
- Signature: gpu_i2c_resume(struct device * dev)
- Line: 343

### gpu_i2c_start
- Return type: static int
- Signature: gpu_i2c_start(struct gpu_i2c_dev * i2cd)
- Line: 142

### gpu_i2c_stop
- Return type: static int
- Signature: gpu_i2c_stop(struct gpu_i2c_dev * i2cd)
- Line: 148

### gpu_i2c_write
- Return type: static int
- Signature: gpu_i2c_write(struct gpu_i2c_dev * i2cd,u8 data)
- Line: 154

### gpu_i2c_xfer
- Return type: static int
- Signature: gpu_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 166

## Structs (1)

### gpu_i2c_dev
- Line: 53
- Members:
  - dev: device *
  - regs: void __iomem *
  - adapter: i2c_adapter
  - gpu_ccgx_ucsi: i2c_board_info *
  - ccgx_client: i2c_client *

## Variables (6)

- static **ccgx_node** : const struct software_node (line 268)
- static **ccgx_props** : const struct property_entry[] (line 260)
- static **gpu_i2c_algorithm** : const struct i2c_algorithm (line 234)
- static **gpu_i2c_driver** : pci_driver (line 361)
- static **gpu_i2c_ids** : const struct pci_device_id[] (line 253)
- static **gpu_i2c_quirks** : const struct i2c_adapter_quirks (line 223)

## Macros (26)

- **I2C_MST_ADDR** (line 38)
- **I2C_MST_CNTL** (line 24)
- **I2C_MST_CNTL_BURST_SIZE_SHIFT** (line 29)
- **I2C_MST_CNTL_CMD_READ** (line 27)
- **I2C_MST_CNTL_CMD_WRITE** (line 28)
- **I2C_MST_CNTL_CYCLE_TRIGGER** (line 36)
- **I2C_MST_CNTL_GEN_NACK** (line 30)
- **I2C_MST_CNTL_GEN_START** (line 25)
- **I2C_MST_CNTL_GEN_STOP** (line 26)
- **I2C_MST_CNTL_STATUS** (line 31)
- **I2C_MST_CNTL_STATUS_BUS_BUSY** (line 35)
- **I2C_MST_CNTL_STATUS_NO_ACK** (line 33)
- **I2C_MST_CNTL_STATUS_OKAY** (line 32)
- **I2C_MST_CNTL_STATUS_TIMEOUT** (line 34)
- **I2C_MST_DATA** (line 46)
- **I2C_MST_HYBRID_PADCTL** (line 48)
- **I2C_MST_HYBRID_PADCTL_I2C_SCL_INPUT_RCV** (line 50)
- **I2C_MST_HYBRID_PADCTL_I2C_SDA_INPUT_RCV** (line 51)
- **I2C_MST_HYBRID_PADCTL_MODE_I2C** (line 49)
- **I2C_MST_I2C0_TIMING** (line 40)
- **I2C_MST_I2C0_TIMING_SCL_PERIOD_100KHZ** (line 41)
- **I2C_MST_I2C0_TIMING_TIMEOUT_CHECK** (line 44)
- **I2C_MST_I2C0_TIMING_TIMEOUT_CLK_CNT** (line 42)
- **I2C_MST_I2C0_TIMING_TIMEOUT_CLK_CNT_MAX** (line 43)
- **PCI_CLASS_SERIAL_UNKNOWN** (line 252)
- **gpu_i2c_suspend** (line 341)
