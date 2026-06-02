# drivers/i2c/busses/i2c-pnx.c

Subsystem: drivers/i2c

## Functions (17)

### bus_reset_if_active
- Return type: static void
- Signature: bus_reset_if_active(struct i2c_pnx_algo_data * alg_data)
- Line: 446

### i2c_adap_pnx_exit
- Return type: static void __exit
- Signature: i2c_adap_pnx_exit(void)
- Line: 744

### i2c_adap_pnx_init
- Return type: static int __init
- Signature: i2c_adap_pnx_init(void)
- Line: 739

### i2c_pnx_controller_resume
- Return type: static int
- Signature: i2c_pnx_controller_resume(struct device * dev)
- Line: 596

### i2c_pnx_controller_suspend
- Return type: static int
- Signature: i2c_pnx_controller_suspend(struct device * dev)
- Line: 587

### i2c_pnx_func
- Return type: static u32
- Signature: i2c_pnx_func(struct i2c_adapter * adapter)
- Line: 577

### i2c_pnx_interrupt
- Return type: static irqreturn_t
- Signature: i2c_pnx_interrupt(int irq,void * dev_id)
- Line: 353

### i2c_pnx_master_rcv
- Return type: static int
- Signature: i2c_pnx_master_rcv(struct i2c_pnx_algo_data * alg_data)
- Line: 276

### i2c_pnx_master_xmit
- Return type: static int
- Signature: i2c_pnx_master_xmit(struct i2c_pnx_algo_data * alg_data)
- Line: 210

### i2c_pnx_probe
- Return type: static int
- Signature: i2c_pnx_probe(struct platform_device * pdev)
- Line: 607

### i2c_pnx_remove
- Return type: static void
- Signature: i2c_pnx_remove(struct platform_device * pdev)
- Line: 713

### i2c_pnx_start
- Return type: static int
- Signature: i2c_pnx_start(unsigned char slave_addr,struct i2c_pnx_algo_data * alg_data)
- Line: 125

### i2c_pnx_stop
- Return type: static void
- Signature: i2c_pnx_stop(struct i2c_pnx_algo_data * alg_data)
- Line: 181

### i2c_pnx_timeout
- Return type: static void
- Signature: i2c_pnx_timeout(struct i2c_pnx_algo_data * alg_data)
- Line: 426

### i2c_pnx_xfer
- Return type: static int
- Signature: i2c_pnx_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 480

### wait_reset
- Return type: static int
- Signature: wait_reset(struct i2c_pnx_algo_data * data)
- Line: 107

### wait_timeout
- Return type: static int
- Signature: wait_timeout(struct i2c_pnx_algo_data * data)
- Line: 96

## Structs (2)

### i2c_pnx_algo_data
- Line: 39
- Members:
  - ret: int
  - mode: int
  - complete: completion
  - buf: u8 *
  - len: int
  - order: int
  - ioaddr: void __iomem *
  - mif: i2c_pnx_mif
  - last: int
  - clk: clk *
  - adapter: i2c_adapter
  - irq: int
  - timeout: u32

### i2c_pnx_mif
- Line: 30
- Members:
  - ret: int
  - mode: int
  - complete: completion
  - buf: u8 *
  - len: int
  - order: int
  - ioaddr: void __iomem *
  - mif: i2c_pnx_mif
  - last: int
  - clk: clk *
  - adapter: i2c_adapter
  - irq: int
  - timeout: u32

## Enums (3)

### __anon245a70200103
- Line: 49

### __anon245a70200203
- Line: 63

### __anon245a70200303
- Line: 76

## Variables (3)

- static **i2c_pnx_driver** : platform_driver (line 729)
- static **i2c_pnx_of_match** : const struct of_device_id[] (line 722)
- static **pnx_algorithm** : const struct i2c_algorithm (line 582)

## Macros (16)

- **I2C_PNX_REGION_SIZE** (line 28)
- **I2C_PNX_SPEED_KHZ_DEFAULT** (line 27)
- **I2C_PNX_TIMEOUT_DEFAULT** (line 26)
- **I2C_REG_ADR**(a) (line 88)
- **I2C_REG_CKH**(a) (line 87)
- **I2C_REG_CKL**(a) (line 86)
- **I2C_REG_CTL**(a) (line 85)
- **I2C_REG_RFL**(a) (line 89)
- **I2C_REG_RX**(a) (line 82)
- **I2C_REG_RXB**(a) (line 91)
- **I2C_REG_STFL**(a) (line 94)
- **I2C_REG_STS**(a) (line 84)
- **I2C_REG_TFL**(a) (line 90)
- **I2C_REG_TX**(a) (line 83)
- **I2C_REG_TXB**(a) (line 92)
- **I2C_REG_TXS**(a) (line 93)
