# drivers/i2c/busses/i2c-viai2c-zhaoxin.c

Subsystem: drivers/i2c

## Functions (9)

### viai2c_fifo_irq_xfer
- Return type: static int
- Signature: viai2c_fifo_irq_xfer(struct viai2c * i2c)
- Line: 92

### viai2c_fifo_xfer
- Return type: static int
- Signature: viai2c_fifo_xfer(struct viai2c * i2c)
- Line: 52

### zxi2c_func
- Return type: static u32
- Signature: zxi2c_func(struct i2c_adapter * adap)
- Line: 191

### zxi2c_get_bus_speed
- Return type: static void
- Signature: zxi2c_get_bus_speed(struct viai2c * i2c)
- Line: 223

### zxi2c_isr
- Return type: static irqreturn_t
- Signature: zxi2c_isr(int irq,void * data)
- Line: 260

### zxi2c_probe
- Return type: static int
- Signature: zxi2c_probe(struct platform_device * pdev)
- Line: 290

### zxi2c_resume
- Return type: static int __maybe_unused
- Signature: zxi2c_resume(struct device * dev)
- Line: 334

### zxi2c_set_bus_speed
- Return type: static void
- Signature: zxi2c_set_bus_speed(struct viai2c * i2c)
- Line: 214

### zxi2c_xfer
- Return type: static int
- Signature: zxi2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 139

## Structs (1)

### viai2c_zhaoxin
- Line: 45
- Members:
  - hrv: u8
  - tr: u16
  - mcr: u16
  - xfer_len: u16

## Variables (6)

- static **zxi2c_acpi_match** : const struct acpi_device_id[] (line 348)
- static **zxi2c_algorithm** : const struct i2c_algorithm (line 196)
- static **zxi2c_driver** : platform_driver (line 354)
- static **zxi2c_pm** : const struct dev_pm_ops (line 344)
- static **zxi2c_quirks** : const struct i2c_adapter_quirks (line 201)
- static **zxi2c_speed_params_table** : const u32[][3] (line 205)

## Macros (22)

- **ZXI2C_CLK_50M** (line 25)
- **ZXI2C_CR_FIFO_MODE** (line 16)
- **ZXI2C_CR_MST_RST** (line 15)
- **ZXI2C_FIFO_SIZE** (line 43)
- **ZXI2C_GOLD_FSTP_100K** (line 37)
- **ZXI2C_GOLD_FSTP_1M** (line 39)
- **ZXI2C_GOLD_FSTP_3400K** (line 40)
- **ZXI2C_GOLD_FSTP_400K** (line 38)
- **ZXI2C_HCR_RST_FIFO** (line 28)
- **ZXI2C_HS_CTRL_CODE** (line 41)
- **ZXI2C_IRQ_FIFOEND** (line 19)
- **ZXI2C_IRQ_FIFONACK** (line 18)
- **ZXI2C_IRQ_MASK** (line 20)
- **ZXI2C_REG_CLK** (line 24)
- **ZXI2C_REG_HCR** (line 27)
- **ZXI2C_REG_HRCNTR** (line 34)
- **ZXI2C_REG_HRDR** (line 30)
- **ZXI2C_REG_HRLR** (line 32)
- **ZXI2C_REG_HTDR** (line 29)
- **ZXI2C_REG_HTLR** (line 31)
- **ZXI2C_REG_HWCNTR** (line 33)
- **ZXI2C_REG_REV** (line 26)
