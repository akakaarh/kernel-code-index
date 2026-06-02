# drivers/spi/spi-bcmbca-hsspi.c

Subsystem: drivers/spi

## Functions (13)

### bcmbca_hsspi_do_txrx
- Return type: static int
- Signature: bcmbca_hsspi_do_txrx(struct spi_device * spi,struct spi_transfer * t,struct spi_message * msg)
- Line: 250

### bcmbca_hsspi_interrupt
- Return type: static irqreturn_t
- Signature: bcmbca_hsspi_interrupt(int irq,void * dev_id)
- Line: 417

### bcmbca_hsspi_probe
- Return type: static int
- Signature: bcmbca_hsspi_probe(struct platform_device * pdev)
- Line: 432

### bcmbca_hsspi_remove
- Return type: static void
- Signature: bcmbca_hsspi_remove(struct platform_device * pdev)
- Line: 554

### bcmbca_hsspi_resume
- Return type: static int
- Signature: bcmbca_hsspi_resume(struct device * dev)
- Line: 579

### bcmbca_hsspi_set_clk
- Return type: static void
- Signature: bcmbca_hsspi_set_clk(struct bcmbca_hsspi * bs,struct spi_device * spi,int hz)
- Line: 193

### bcmbca_hsspi_set_cs
- Return type: static void
- Signature: bcmbca_hsspi_set_cs(struct bcmbca_hsspi * bs,unsigned int cs,bool active)
- Line: 171

### bcmbca_hsspi_setup
- Return type: static int
- Signature: bcmbca_hsspi_setup(struct spi_device * spi)
- Line: 329

### bcmbca_hsspi_suspend
- Return type: static int
- Signature: bcmbca_hsspi_suspend(struct device * dev)
- Line: 567

### bcmbca_hsspi_transfer_one
- Return type: static int
- Signature: bcmbca_hsspi_transfer_one(struct spi_controller * host,struct spi_message * msg)
- Line: 369

### bcmbca_hsspi_wait_cmd
- Return type: static int
- Signature: bcmbca_hsspi_wait_cmd(struct bcmbca_hsspi * bs,unsigned int cs)
- Line: 221

### wait_mode_show
- Return type: static ssize_t
- Signature: wait_mode_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 126

### wait_mode_store
- Return type: static ssize_t
- Signature: wait_mode_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 135

## Structs (1)

### bcmbca_hsspi
- Line: 111
- Members:
  - done: completion
  - bus_mutex: mutex
  - msg_mutex: mutex
  - pdev: platform_device *
  - clk: clk *
  - pll_clk: clk *
  - regs: void __iomem *
  - spim_ctrl: void __iomem *
  - fifo: u8 __iomem *
  - speed_hz: u32
  - cs_polarity: u8
  - wait_mode: u32

## Variables (4)

- static **bcmbca_hsspi_attrs** : attribute * [] (line 162)
- static **bcmbca_hsspi_driver** : platform_driver (line 613)
- static **bcmbca_hsspi_group** : const struct attribute_group (line 167)
- static **bcmbca_hsspi_of_match** : const struct of_device_id[] (line 606)

## Macros (67)

- **CLK_CTRL_ACCUM_RST_ON_LOOP** (line 65)
- **CLK_CTRL_CLK_POLARITY** (line 66)
- **CLK_CTRL_FREQ_CTRL_MASK** (line 63)
- **CLK_CTRL_SPI_CLK_2X_SEL** (line 64)
- **GLOBAL_CTRL_CLK_GATE_SSOFF** (line 31)
- **GLOBAL_CTRL_CLK_POLARITY** (line 32)
- **GLOBAL_CTRL_CS_POLARITY_MASK** (line 28)
- **GLOBAL_CTRL_CS_POLARITY_SHIFT** (line 27)
- **GLOBAL_CTRL_MOSI_IDLE** (line 33)
- **GLOBAL_CTRL_PLL_CLK_CTRL_MASK** (line 30)
- **GLOBAL_CTRL_PLL_CLK_CTRL_SHIFT** (line 29)
- **HSSPI_BUFFER_LEN** (line 91)
- **HSSPI_BUS_NUM** (line 99)
- **HSSPI_FIFO_REG**(x) (line 81)
- **HSSPI_GLOBAL_CTRL_REG** (line 26)
- **HSSPI_GLOBAL_EXT_TRIGGER_REG** (line 35)
- **HSSPI_INT_CLEAR_ALL** (line 47)
- **HSSPI_INT_MASK_REG** (line 39)
- **HSSPI_INT_STATUS_MASKED_REG** (line 38)
- **HSSPI_INT_STATUS_REG** (line 37)
- **HSSPI_MAX_PREPEND_LEN** (line 94)
- **HSSPI_MAX_SYNC_CLOCK** (line 96)
- **HSSPI_OPCODE_LEN** (line 92)
- **HSSPI_OP_CODE_SHIFT** (line 84)
- **HSSPI_OP_MULTIBIT** (line 83)
- **HSSPI_OP_READ** (line 88)
- **HSSPI_OP_READ_WRITE** (line 86)
- **HSSPI_OP_SETIRQ** (line 89)
- **HSSPI_OP_SLEEP** (line 85)
- **HSSPI_OP_WRITE** (line 87)
- **HSSPI_PINGPONG_COMMAND_REG**(x) (line 49)
- **HSSPI_PINGPONG_STATUS_REG**(x) (line 59)
- **HSSPI_PINGPONG_STATUS_SRC_BUSY** (line 60)
- **HSSPI_PINGx_CMD_DONE**(i) (line 41)
- **HSSPI_PINGx_CTRL_INVAL**(i) (line 45)
- **HSSPI_PINGx_POLL_TIMEOUT**(i) (line 44)
- **HSSPI_PINGx_RX_OVER**(i) (line 42)
- **HSSPI_PINGx_TX_UNDER**(i) (line 43)
- **HSSPI_POLL_STATUS_TIMEOUT_MS** (line 100)
- **HSSPI_PROFILE_CLK_CTRL_REG**(x) (line 62)
- **HSSPI_PROFILE_MODE_CTRL_REG**(x) (line 73)
- **HSSPI_PROFILE_SIGNAL_CTRL_REG**(x) (line 68)
- **HSSPI_SPI_MAX_CS** (line 98)
- **HSSPI_WAIT_MODE_INTR** (line 103)
- **HSSPI_WAIT_MODE_MAX** (line 104)
- **HSSPI_WAIT_MODE_POLLING** (line 102)
- **MODE_CTRL_MODE_3WIRE** (line 78)
- **MODE_CTRL_MULTIDATA_RD_SIZE_SHIFT** (line 76)
- **MODE_CTRL_MULTIDATA_RD_STRT_SHIFT** (line 74)
- **MODE_CTRL_MULTIDATA_WR_SIZE_SHIFT** (line 77)
- **MODE_CTRL_MULTIDATA_WR_STRT_SHIFT** (line 75)
- **MODE_CTRL_PREPENDBYTE_CNT_SHIFT** (line 79)
- **PINGPONG_CMD_COMMAND_MASK** (line 50)
- **PINGPONG_CMD_PROFILE_SHIFT** (line 56)
- **PINGPONG_CMD_SS_SHIFT** (line 57)
- **PINGPONG_COMMAND_FLUSH** (line 55)
- **PINGPONG_COMMAND_HALT** (line 54)
- **PINGPONG_COMMAND_NOOP** (line 51)
- **PINGPONG_COMMAND_START_NOW** (line 52)
- **PINGPONG_COMMAND_START_TRIGGER** (line 53)
- **SIGNAL_CTRL_ASYNC_INPUT_PATH** (line 71)
- **SIGNAL_CTRL_LATCH_RISING** (line 69)
- **SIGNAL_CTRL_LAUNCH_RISING** (line 70)
- **SPIM_CTRL_CS_OVERRIDE_SEL_MASK** (line 107)
- **SPIM_CTRL_CS_OVERRIDE_SEL_SHIFT** (line 106)
- **SPIM_CTRL_CS_OVERRIDE_VAL_MASK** (line 109)
- **SPIM_CTRL_CS_OVERRIDE_VAL_SHIFT** (line 108)
