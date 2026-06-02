# drivers/i2c/busses/i2c-ocores.c

Subsystem: drivers/i2c

## Functions (30)

### oc_getreg
- Return type: static u8
- Signature: oc_getreg(struct ocores_i2c * i2c,int reg)
- Line: 144

### oc_getreg_16
- Return type: static u8
- Signature: oc_getreg_16(struct ocores_i2c * i2c,int reg)
- Line: 119

### oc_getreg_16be
- Return type: static u8
- Signature: oc_getreg_16be(struct ocores_i2c * i2c,int reg)
- Line: 129

### oc_getreg_32
- Return type: static u8
- Signature: oc_getreg_32(struct ocores_i2c * i2c,int reg)
- Line: 124

### oc_getreg_32be
- Return type: static u8
- Signature: oc_getreg_32be(struct ocores_i2c * i2c,int reg)
- Line: 134

### oc_getreg_8
- Return type: static u8
- Signature: oc_getreg_8(struct ocores_i2c * i2c,int reg)
- Line: 114

### oc_getreg_grlib
- Return type: static u8
- Signature: oc_getreg_grlib(struct ocores_i2c * i2c,int reg)
- Line: 478

### oc_setreg
- Return type: static void
- Signature: oc_setreg(struct ocores_i2c * i2c,int reg,u8 value)
- Line: 139

### oc_setreg_16
- Return type: static void
- Signature: oc_setreg_16(struct ocores_i2c * i2c,int reg,u8 value)
- Line: 94

### oc_setreg_16be
- Return type: static void
- Signature: oc_setreg_16be(struct ocores_i2c * i2c,int reg,u8 value)
- Line: 104

### oc_setreg_32
- Return type: static void
- Signature: oc_setreg_32(struct ocores_i2c * i2c,int reg,u8 value)
- Line: 99

### oc_setreg_32be
- Return type: static void
- Signature: oc_setreg_32be(struct ocores_i2c * i2c,int reg,u8 value)
- Line: 109

### oc_setreg_8
- Return type: static void
- Signature: oc_setreg_8(struct ocores_i2c * i2c,int reg,u8 value)
- Line: 89

### oc_setreg_grlib
- Return type: static void
- Signature: oc_setreg_grlib(struct ocores_i2c * i2c,int reg,u8 value)
- Line: 492

### ocores_func
- Return type: static u32
- Signature: ocores_func(struct i2c_adapter * adap)
- Line: 435

### ocores_i2c_of_probe
- Return type: static int
- Signature: ocores_i2c_of_probe(struct platform_device * pdev,struct ocores_i2c * i2c)
- Line: 511

### ocores_i2c_probe
- Return type: static int
- Signature: ocores_i2c_probe(struct platform_device * pdev)
- Line: 580

### ocores_i2c_remove
- Return type: static void
- Signature: ocores_i2c_remove(struct platform_device * pdev)
- Line: 720

### ocores_i2c_resume
- Return type: static int
- Signature: ocores_i2c_resume(struct device * dev)
- Line: 746

### ocores_i2c_suspend
- Return type: static int
- Signature: ocores_i2c_suspend(struct device * dev)
- Line: 733

### ocores_init
- Return type: static int
- Signature: ocores_init(struct device * dev,struct ocores_i2c * i2c)
- Line: 403

### ocores_isr
- Return type: static irqreturn_t
- Signature: ocores_isr(int irq,void * dev_id)
- Line: 226

### ocores_poll_wait
- Return type: static int
- Signature: ocores_poll_wait(struct ocores_i2c * i2c)
- Line: 289

### ocores_process
- Return type: static void
- Signature: ocores_process(struct ocores_i2c * i2c,u8 stat)
- Line: 149

### ocores_process_polling
- Return type: static int
- Signature: ocores_process_polling(struct ocores_i2c * i2c)
- Line: 331

### ocores_process_timeout
- Return type: static void
- Signature: ocores_process_timeout(struct ocores_i2c * i2c)
- Line: 246

### ocores_wait
- Return type: static int
- Signature: ocores_wait(struct ocores_i2c * i2c,int reg,u8 mask,u8 val,unsigned long timeout_us)
- Line: 269

### ocores_xfer
- Return type: static int
- Signature: ocores_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 397

### ocores_xfer_core
- Return type: static int
- Signature: ocores_xfer_core(struct ocores_i2c * i2c,struct i2c_msg * msgs,int num,bool polling)
- Line: 354

### ocores_xfer_polling
- Return type: static int
- Signature: ocores_xfer_polling(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 391

## Structs (1)

### ocores_i2c
- Line: 34
- Members:
  - base: void __iomem *
  - reg_shift: u32
  - reg_io_width: u32
  - flags: unsigned long
  - wait: wait_queue_head_t
  - adap: i2c_adapter
  - msg: i2c_msg *
  - pos: int
  - nmsgs: int
  - state: int
  - process_lock: spinlock_t
  - clk: clk *
  - ip_clock_khz: int
  - bus_clock_khz: int
  - setreg: void (*)(struct ocores_i2c * i2c,int reg,u8 value)
  - getreg: u8 (*)(struct ocores_i2c * i2c,int reg)

## Variables (4)

- static **ocores_adapter** : const struct i2c_adapter (line 446)
- static **ocores_algorithm** : i2c_algorithm (line 440)
- static **ocores_i2c_driver** : platform_driver (line 764)
- static **ocores_i2c_match** : const struct of_device_id[] (line 453)

## Macros (29)

- **OCI2C_CMD** (line 58)
- **OCI2C_CMD_IACK** (line 70)
- **OCI2C_CMD_READ** (line 66)
- **OCI2C_CMD_READ_ACK** (line 68)
- **OCI2C_CMD_READ_NACK** (line 69)
- **OCI2C_CMD_START** (line 64)
- **OCI2C_CMD_STOP** (line 65)
- **OCI2C_CMD_WRITE** (line 67)
- **OCI2C_CONTROL** (line 56)
- **OCI2C_CTRL_EN** (line 62)
- **OCI2C_CTRL_IEN** (line 61)
- **OCI2C_DATA** (line 57)
- **OCI2C_PREHIGH** (line 55)
- **OCI2C_PRELOW** (line 54)
- **OCI2C_STATUS** (line 59)
- **OCI2C_STAT_ARBLOST** (line 74)
- **OCI2C_STAT_BUSY** (line 75)
- **OCI2C_STAT_IF** (line 72)
- **OCI2C_STAT_NACK** (line 76)
- **OCI2C_STAT_TIP** (line 73)
- **OCORES_FLAG_BROKEN_IRQ** (line 87)
- **STATE_DONE** (line 78)
- **STATE_ERROR** (line 82)
- **STATE_READ** (line 81)
- **STATE_START** (line 79)
- **STATE_WRITE** (line 80)
- **TYPE_GRLIB** (line 85)
- **TYPE_OCORES** (line 84)
- **ocores_i2c_of_probe**(pdev,i2c) (line 577)
