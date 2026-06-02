# drivers/i2c/busses/i2c-mxs.c

Subsystem: drivers/i2c

## Functions (19)

### mxs_i2c_derive_timing
- Return type: static void
- Signature: mxs_i2c_derive_timing(struct mxs_i2c_dev * i2c,uint32_t speed)
- Line: 698

### mxs_i2c_dma_finish
- Return type: static void
- Signature: mxs_i2c_dma_finish(struct mxs_i2c_dev * i2c)
- Line: 154

### mxs_i2c_dma_irq_callback
- Return type: static void
- Signature: mxs_i2c_dma_irq_callback(void * param)
- Line: 164

### mxs_i2c_dma_setup_xfer
- Return type: static int
- Signature: mxs_i2c_dma_setup_xfer(struct i2c_adapter * adap,struct i2c_msg * msg,u8 * buf,uint32_t flags)
- Line: 172

### mxs_i2c_exit
- Return type: static void __exit
- Signature: mxs_i2c_exit(void)
- Line: 893

### mxs_i2c_func
- Return type: static u32
- Signature: mxs_i2c_func(struct i2c_adapter * adap)
- Line: 663

### mxs_i2c_get_ofdata
- Return type: static int
- Signature: mxs_i2c_get_ofdata(struct mxs_i2c_dev * i2c)
- Line: 773

### mxs_i2c_init
- Return type: static int __init
- Signature: mxs_i2c_init(void)
- Line: 887

### mxs_i2c_isr
- Return type: static irqreturn_t
- Signature: mxs_i2c_isr(int this_irq,void * dev_id)
- Line: 668

### mxs_i2c_pio_check_error_state
- Return type: static int
- Signature: mxs_i2c_pio_check_error_state(struct mxs_i2c_dev * i2c)
- Line: 319

### mxs_i2c_pio_setup_xfer
- Return type: static int
- Signature: mxs_i2c_pio_setup_xfer(struct i2c_adapter * adap,struct i2c_msg * msg,uint32_t flags)
- Line: 368

### mxs_i2c_pio_trigger_cmd
- Return type: static void
- Signature: mxs_i2c_pio_trigger_cmd(struct mxs_i2c_dev * i2c,u32 cmd)
- Line: 336

### mxs_i2c_pio_trigger_write_cmd
- Return type: static void
- Signature: mxs_i2c_pio_trigger_write_cmd(struct mxs_i2c_dev * i2c,u32 cmd,u32 data)
- Line: 356

### mxs_i2c_pio_wait_xfer_end
- Return type: static int
- Signature: mxs_i2c_pio_wait_xfer_end(struct mxs_i2c_dev * i2c)
- Line: 303

### mxs_i2c_probe
- Return type: static int
- Signature: mxs_i2c_probe(struct platform_device * pdev)
- Line: 798

### mxs_i2c_remove
- Return type: static void
- Signature: mxs_i2c_remove(struct platform_device * pdev)
- Line: 866

### mxs_i2c_reset
- Return type: static int
- Signature: mxs_i2c_reset(struct mxs_i2c_dev * i2c)
- Line: 132

### mxs_i2c_xfer
- Return type: static int
- Signature: mxs_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 648

### mxs_i2c_xfer_msg
- Return type: static int
- Signature: mxs_i2c_xfer_msg(struct i2c_adapter * adap,struct i2c_msg * msg,int stop)
- Line: 559

## Structs (1)

### mxs_i2c_dev
- Line: 112
- Members:
  - dev: device *
  - dev_type: mxs_i2c_devtype
  - regs: void __iomem *
  - cmd_complete: completion
  - cmd_err: int
  - adapter: i2c_adapter
  - timing0: uint32_t
  - timing1: uint32_t
  - timing2: uint32_t
  - dmach: dma_chan *
  - pio_data: uint32_t[2]
  - addr_data: uint32_t
  - sg_io: scatterlist[2]
  - dma_read: bool

## Enums (1)

### mxs_i2c_devtype
- Line: 96

## Variables (4)

- static **mxs_i2c_algo** : const struct i2c_algorithm (line 689)
- static **mxs_i2c_driver** : platform_driver (line 878)
- static **mxs_i2c_dt_ids** : const struct of_device_id[] (line 791)
- static **mxs_i2c_quirks** : const struct i2c_adapter_quirks (line 694)

## Macros (40)

- **DRIVER_NAME** (line 29)
- **MXS_CMD_I2C_READ** (line 93)
- **MXS_CMD_I2C_SELECT** (line 83)
- **MXS_CMD_I2C_WRITE** (line 89)
- **MXS_I2C_CTRL0** (line 31)
- **MXS_I2C_CTRL0_CLR** (line 33)
- **MXS_I2C_CTRL0_DIRECTION** (line 43)
- **MXS_I2C_CTRL0_MASTER_MODE** (line 42)
- **MXS_I2C_CTRL0_PIO_MODE** (line 38)
- **MXS_I2C_CTRL0_POST_SEND_STOP** (line 40)
- **MXS_I2C_CTRL0_PRE_SEND_START** (line 41)
- **MXS_I2C_CTRL0_RETAIN_CLOCK** (line 39)
- **MXS_I2C_CTRL0_RUN** (line 36)
- **MXS_I2C_CTRL0_SEND_NAK_ON_LAST** (line 37)
- **MXS_I2C_CTRL0_SET** (line 32)
- **MXS_I2C_CTRL0_SFTRST** (line 35)
- **MXS_I2C_CTRL0_XFER_COUNT**(v) (line 44)
- **MXS_I2C_CTRL1** (line 50)
- **MXS_I2C_CTRL1_BUS_FREE_IRQ** (line 55)
- **MXS_I2C_CTRL1_CLR** (line 52)
- **MXS_I2C_CTRL1_CLR_GOT_A_NAK** (line 54)
- **MXS_I2C_CTRL1_DATA_ENGINE_CMPLT_IRQ** (line 56)
- **MXS_I2C_CTRL1_EARLY_TERM_IRQ** (line 59)
- **MXS_I2C_CTRL1_MASTER_LOSS_IRQ** (line 60)
- **MXS_I2C_CTRL1_NO_SLAVE_ACK_IRQ** (line 57)
- **MXS_I2C_CTRL1_OVERSIZE_XFER_TERM_IRQ** (line 58)
- **MXS_I2C_CTRL1_SET** (line 51)
- **MXS_I2C_CTRL1_SLAVE_IRQ** (line 62)
- **MXS_I2C_CTRL1_SLAVE_STOP_IRQ** (line 61)
- **MXS_I2C_DATA**(i2c) (line 69)
- **MXS_I2C_DEBUG0_CLR**(i2c) (line 71)
- **MXS_I2C_DEBUG0_DMAREQ** (line 73)
- **MXS_I2C_IRQ_MASK** (line 75)
- **MXS_I2C_STAT** (line 64)
- **MXS_I2C_STAT_BUS_BUSY** (line 66)
- **MXS_I2C_STAT_CLK_GEN_BUSY** (line 67)
- **MXS_I2C_STAT_GOT_A_NAK** (line 65)
- **MXS_I2C_TIMING0** (line 46)
- **MXS_I2C_TIMING1** (line 47)
- **MXS_I2C_TIMING2** (line 48)
