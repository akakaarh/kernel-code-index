# drivers/spi/spi-bcm63xx-hsspi.c

Subsystem: drivers/spi

## Functions (20)

### bcm63xx_hsspi_do_dummy_cs_txrx
- Return type: static int
- Signature: bcm63xx_hsspi_do_dummy_cs_txrx(struct spi_device * spi,struct spi_message * msg)
- Line: 604

### bcm63xx_hsspi_do_prepend_txrx
- Return type: static int
- Signature: bcm63xx_hsspi_do_prepend_txrx(struct spi_device * spi,struct spi_transfer * t)
- Line: 373

### bcm63xx_hsspi_do_txrx
- Return type: static int
- Signature: bcm63xx_hsspi_do_txrx(struct spi_device * spi,struct spi_transfer * t)
- Line: 493

### bcm63xx_hsspi_interrupt
- Return type: static irqreturn_t
- Signature: bcm63xx_hsspi_interrupt(int irq,void * dev_id)
- Line: 727

### bcm63xx_hsspi_max_message_size
- Return type: static size_t
- Signature: bcm63xx_hsspi_max_message_size(struct spi_device * spi)
- Line: 231

### bcm63xx_hsspi_mem_supports_op
- Return type: static bool
- Signature: bcm63xx_hsspi_mem_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 714

### bcm63xx_hsspi_probe
- Return type: static int
- Signature: bcm63xx_hsspi_probe(struct platform_device * pdev)
- Line: 742

### bcm63xx_hsspi_remove
- Return type: static void
- Signature: bcm63xx_hsspi_remove(struct platform_device * pdev)
- Line: 878

### bcm63xx_hsspi_resume
- Return type: static int
- Signature: bcm63xx_hsspi_resume(struct device * dev)
- Line: 907

### bcm63xx_hsspi_set_clk
- Return type: static void
- Signature: bcm63xx_hsspi_set_clk(struct bcm63xx_hsspi * bs,struct spi_device * spi,int hz)
- Line: 466

### bcm63xx_hsspi_set_cs
- Return type: static void
- Signature: bcm63xx_hsspi_set_cs(struct bcm63xx_hsspi * bs,unsigned int cs,bool active)
- Line: 450

### bcm63xx_hsspi_setup
- Return type: static int
- Signature: bcm63xx_hsspi_setup(struct spi_device * spi)
- Line: 567

### bcm63xx_hsspi_suspend
- Return type: static int
- Signature: bcm63xx_hsspi_suspend(struct device * dev)
- Line: 895

### bcm63xx_hsspi_transfer_one
- Return type: static int
- Signature: bcm63xx_hsspi_transfer_one(struct spi_controller * host,struct spi_message * msg)
- Line: 681

### bcm63xx_hsspi_wait_cmd
- Return type: static int
- Signature: bcm63xx_hsspi_wait_cmd(struct bcm63xx_hsspi * bs)
- Line: 236

### bcm63xx_prepare_prepend_transfer
- Return type: static bool
- Signature: bcm63xx_prepare_prepend_transfer(struct spi_controller * host,struct spi_message * msg,struct spi_transfer * t_prepend)
- Line: 266

### wait_mode_show
- Return type: static ssize_t
- Signature: wait_mode_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 149

### wait_mode_store
- Return type: static ssize_t
- Signature: wait_mode_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 158

### xfer_mode_show
- Return type: static ssize_t
- Signature: xfer_mode_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 185

### xfer_mode_store
- Return type: static ssize_t
- Signature: xfer_mode_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 194

## Structs (1)

### bcm63xx_hsspi
- Line: 130
- Members:
  - done: completion
  - bus_mutex: mutex
  - msg_mutex: mutex
  - pdev: platform_device *
  - clk: clk *
  - pll_clk: clk *
  - regs: void __iomem *
  - fifo: u8 __iomem *
  - speed_hz: u32
  - cs_polarity: u8
  - wait_mode: u32
  - xfer_mode: u32
  - prepend_cnt: u32
  - md_start: u32
  - prepend_buf: u8 *

## Variables (5)

- static **bcm63xx_hsspi_attrs** : attribute * [] (line 218)
- static **bcm63xx_hsspi_driver** : platform_driver (line 941)
- static **bcm63xx_hsspi_group** : const struct attribute_group (line 224)
- static **bcm63xx_hsspi_mem_ops** : const struct spi_controller_mem_ops (line 723)
- static **bcm63xx_hsspi_of_match** : const struct of_device_id[] (line 934)

## Macros (67)

- **CLK_CTRL_ACCUM_RST_ON_LOOP** (line 67)
- **CLK_CTRL_FREQ_CTRL_MASK** (line 65)
- **CLK_CTRL_SPI_CLK_2X_SEL** (line 66)
- **GLOBAL_CTRL_CLK_GATE_SSOFF** (line 33)
- **GLOBAL_CTRL_CLK_POLARITY** (line 34)
- **GLOBAL_CTRL_CS_POLARITY_MASK** (line 30)
- **GLOBAL_CTRL_CS_POLARITY_SHIFT** (line 29)
- **GLOBAL_CTRL_MOSI_IDLE** (line 35)
- **GLOBAL_CTRL_PLL_CLK_CTRL_MASK** (line 32)
- **GLOBAL_CTRL_PLL_CLK_CTRL_SHIFT** (line 31)
- **HSSPI_BUFFER_LEN** (line 93)
- **HSSPI_BUS_NUM** (line 105)
- **HSSPI_FIFO_REG**(x) (line 82)
- **HSSPI_GLOBAL_CTRL_REG** (line 28)
- **HSSPI_GLOBAL_EXT_TRIGGER_REG** (line 37)
- **HSSPI_INT_CLEAR_ALL** (line 49)
- **HSSPI_INT_MASK_REG** (line 41)
- **HSSPI_INT_STATUS_MASKED_REG** (line 40)
- **HSSPI_INT_STATUS_REG** (line 39)
- **HSSPI_MAX_PREPEND_LEN** (line 96)
- **HSSPI_MAX_SYNC_CLOCK** (line 102)
- **HSSPI_OPCODE_LEN** (line 94)
- **HSSPI_OP_CODE_SHIFT** (line 86)
- **HSSPI_OP_MULTIBIT** (line 85)
- **HSSPI_OP_READ** (line 90)
- **HSSPI_OP_READ_WRITE** (line 88)
- **HSSPI_OP_SETIRQ** (line 91)
- **HSSPI_OP_SLEEP** (line 87)
- **HSSPI_OP_WRITE** (line 89)
- **HSSPI_PINGPONG_COMMAND_REG**(x) (line 51)
- **HSSPI_PINGPONG_STATUS_REG**(x) (line 61)
- **HSSPI_PINGPONG_STATUS_SRC_BUSY** (line 62)
- **HSSPI_PINGx_CMD_DONE**(i) (line 43)
- **HSSPI_PINGx_CTRL_INVAL**(i) (line 47)
- **HSSPI_PINGx_POLL_TIMEOUT**(i) (line 46)
- **HSSPI_PINGx_RX_OVER**(i) (line 44)
- **HSSPI_PINGx_TX_UNDER**(i) (line 45)
- **HSSPI_POLL_STATUS_TIMEOUT_MS** (line 106)
- **HSSPI_PROFILE_CLK_CTRL_REG**(x) (line 64)
- **HSSPI_PROFILE_MODE_CTRL_REG**(x) (line 74)
- **HSSPI_PROFILE_SIGNAL_CTRL_REG**(x) (line 69)
- **HSSPI_SPI_MAX_CS** (line 104)
- **HSSPI_WAIT_MODE_INTR** (line 109)
- **HSSPI_WAIT_MODE_MAX** (line 110)
- **HSSPI_WAIT_MODE_POLLING** (line 108)
- **HSSPI_XFER_MODE_AUTO** (line 117)
- **HSSPI_XFER_MODE_DUMMYCS** (line 119)
- **HSSPI_XFER_MODE_MAX** (line 120)
- **HSSPI_XFER_MODE_PREPEND** (line 118)
- **MODE_CTRL_MODE_3WIRE** (line 79)
- **MODE_CTRL_MULTIDATA_RD_SIZE_SHIFT** (line 77)
- **MODE_CTRL_MULTIDATA_RD_STRT_SHIFT** (line 75)
- **MODE_CTRL_MULTIDATA_WR_SIZE_SHIFT** (line 78)
- **MODE_CTRL_MULTIDATA_WR_STRT_SHIFT** (line 76)
- **MODE_CTRL_PREPENDBYTE_CNT_SHIFT** (line 80)
- **PINGPONG_CMD_COMMAND_MASK** (line 52)
- **PINGPONG_CMD_PROFILE_SHIFT** (line 58)
- **PINGPONG_CMD_SS_SHIFT** (line 59)
- **PINGPONG_COMMAND_FLUSH** (line 57)
- **PINGPONG_COMMAND_HALT** (line 56)
- **PINGPONG_COMMAND_NOOP** (line 53)
- **PINGPONG_COMMAND_START_NOW** (line 54)
- **PINGPONG_COMMAND_START_TRIGGER** (line 55)
- **SIGNAL_CTRL_ASYNC_INPUT_PATH** (line 72)
- **SIGNAL_CTRL_LATCH_RISING** (line 70)
- **SIGNAL_CTRL_LAUNCH_RISING** (line 71)
- **bcm63xx_prepend_printk_on_checkfail**(bs,fmt,...) (line 122)
