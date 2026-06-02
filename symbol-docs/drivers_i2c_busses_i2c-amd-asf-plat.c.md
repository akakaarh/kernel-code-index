# drivers/i2c/busses/i2c-amd-asf-plat.c

Subsystem: drivers/i2c

## Functions (11)

### amd_asf_access
- Return type: static int
- Signature: amd_asf_access(struct i2c_adapter * adap,u16 addr,u8 command,u8 * data)
- Line: 163

### amd_asf_func
- Return type: static u32
- Signature: amd_asf_func(struct i2c_adapter * adapter)
- Line: 268

### amd_asf_irq_handler
- Return type: static irqreturn_t
- Signature: amd_asf_irq_handler(int irq,void * ptr)
- Line: 281

### amd_asf_probe
- Return type: static int
- Signature: amd_asf_probe(struct platform_device * pdev)
- Line: 300

### amd_asf_process_target
- Return type: static void
- Signature: amd_asf_process_target(struct work_struct * work)
- Line: 58

### amd_asf_reg_target
- Return type: static int
- Signature: amd_asf_reg_target(struct i2c_client * target)
- Line: 231

### amd_asf_setup_target
- Return type: static void
- Signature: amd_asf_setup_target(struct amd_asf_dev * dev)
- Line: 141

### amd_asf_unreg_target
- Return type: static int
- Signature: amd_asf_unreg_target(struct i2c_client * target)
- Line: 256

### amd_asf_update_ioport_target
- Return type: static void
- Signature: amd_asf_update_ioport_target(unsigned short piix4_smba,u8 bit,unsigned long offset,bool set)
- Line: 122

### amd_asf_update_mmio_target
- Return type: static void
- Signature: amd_asf_update_mmio_target(struct amd_asf_dev * dev,u8 bit,bool set)
- Line: 132

### amd_asf_xfer
- Return type: static int
- Signature: amd_asf_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 189

## Structs (1)

### amd_asf_dev
- Line: 49
- Members:
  - adap: i2c_adapter
  - eoi_base: void __iomem *
  - target: i2c_client *
  - work_buf: delayed_work
  - mmio_cfg: sb800_mmio_cfg
  - port_addr: resource *

## Variables (3)

- static **amd_asf_acpi_ids** : const struct acpi_device_id[] (line 353)
- static **amd_asf_driver** : platform_driver (line 359)
- static **amd_asf_smbus_algorithm** : const struct i2c_algorithm (line 274)

## Macros (17)

- **ASFDATABNKSEL** (line 43)
- **ASFDATARWPTR** (line 41)
- **ASFINDEX** (line 37)
- **ASFLISADDR** (line 38)
- **ASFSETDATARDPTR** (line 42)
- **ASFSLVEN** (line 44)
- **ASFSLVSTA** (line 40)
- **ASFSTA** (line 39)
- **ASF_BLOCK_MAX_BYTES** (line 46)
- **ASF_CLK_EN** (line 34)
- **ASF_DATA_EN** (line 32)
- **ASF_ERROR_STATUS** (line 47)
- **ASF_MSTR_EN** (line 33)
- **ASF_PEC_SP** (line 31)
- **ASF_SLV_INTR** (line 29)
- **ASF_SLV_LISTN** (line 28)
- **ASF_SLV_RST** (line 30)
