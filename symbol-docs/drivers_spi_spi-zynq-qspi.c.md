# drivers/spi/spi-zynq-qspi.c

Subsystem: drivers/spi

## Functions (15)

### zynq_qspi_chipselect
- Return type: static void
- Signature: zynq_qspi_chipselect(struct spi_device * spi,bool assert)
- Line: 290

### zynq_qspi_config_op
- Return type: static int
- Signature: zynq_qspi_config_op(struct zynq_qspi * xqspi,struct spi_device * spi,const struct spi_mem_op * op)
- Line: 335

### zynq_qspi_exec_mem_op
- Return type: static int
- Signature: zynq_qspi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 525

### zynq_qspi_init_hw
- Return type: static void
- Signature: zynq_qspi_init_hw(struct zynq_qspi * xqspi,unsigned int num_cs)
- Line: 181

### zynq_qspi_irq
- Return type: static irqreturn_t
- Signature: zynq_qspi_irq(int irq,void * dev_id)
- Line: 473

### zynq_qspi_probe
- Return type: static int
- Signature: zynq_qspi_probe(struct platform_device * pdev)
- Line: 631

### zynq_qspi_read
- Return type: static u32
- Signature: zynq_qspi_read(struct zynq_qspi * xqspi,u32 offset)
- Line: 149

### zynq_qspi_read_op
- Return type: static void
- Signature: zynq_qspi_read_op(struct zynq_qspi * xqspi,int rxcount)
- Line: 439

### zynq_qspi_remove
- Return type: static void
- Signature: zynq_qspi_remove(struct platform_device * pdev)
- Line: 729

### zynq_qspi_rxfifo_op
- Return type: static void
- Signature: zynq_qspi_rxfifo_op(struct zynq_qspi * xqspi,unsigned int size)
- Line: 245

### zynq_qspi_setup_op
- Return type: static int
- Signature: zynq_qspi_setup_op(struct spi_device * spi)
- Line: 380

### zynq_qspi_supports_op
- Return type: static bool
- Signature: zynq_qspi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 225

### zynq_qspi_txfifo_op
- Return type: static void
- Signature: zynq_qspi_txfifo_op(struct zynq_qspi * xqspi,unsigned int size)
- Line: 266

### zynq_qspi_write
- Return type: static void
- Signature: zynq_qspi_write(struct zynq_qspi * xqspi,u32 offset,u32 val)
- Line: 154

### zynq_qspi_write_op
- Return type: static void
- Signature: zynq_qspi_write_op(struct zynq_qspi * xqspi,int txcount,bool txempty)
- Line: 400

## Structs (1)

### zynq_qspi
- Line: 133
- Members:
  - dev: device *
  - regs: void __iomem *
  - refclk: clk *
  - pclk: clk *
  - irq: int
  - txbuf: u8 *
  - rxbuf: u8 *
  - tx_bytes: int
  - rx_bytes: int
  - data_completion: completion

## Variables (4)

- static **zynq_qspi_driver** : platform_driver (line 753)
- static **zynq_qspi_mem_caps** : const struct spi_controller_mem_caps (line 619)
- static **zynq_qspi_mem_ops** : const struct spi_controller_mem_ops (line 614)
- static **zynq_qspi_of_match** : const struct of_device_id[] (line 743)

## Macros (49)

- **ZYNQ_QSPI_CONFIG_BAUD_DIV_MAX** (line 62)
- **ZYNQ_QSPI_CONFIG_BAUD_DIV_SHIFT** (line 63)
- **ZYNQ_QSPI_CONFIG_BDRATE_MASK** (line 50)
- **ZYNQ_QSPI_CONFIG_CPHA_MASK** (line 51)
- **ZYNQ_QSPI_CONFIG_CPOL_MASK** (line 52)
- **ZYNQ_QSPI_CONFIG_FWIDTH_MASK** (line 53)
- **ZYNQ_QSPI_CONFIG_IFMODE_MASK** (line 46)
- **ZYNQ_QSPI_CONFIG_MANSRTEN_MASK** (line 48)
- **ZYNQ_QSPI_CONFIG_MANSRT_MASK** (line 47)
- **ZYNQ_QSPI_CONFIG_MSTREN_MASK** (line 54)
- **ZYNQ_QSPI_CONFIG_OFFSET** (line 21)
- **ZYNQ_QSPI_CONFIG_PCS** (line 64)
- **ZYNQ_QSPI_CONFIG_SSFORCE_MASK** (line 49)
- **ZYNQ_QSPI_DELAY_OFFSET** (line 27)
- **ZYNQ_QSPI_ENABLE_ENABLE_MASK** (line 92)
- **ZYNQ_QSPI_ENABLE_OFFSET** (line 26)
- **ZYNQ_QSPI_FAST_READ_QOUT_CODE** (line 106)
- **ZYNQ_QSPI_FIFO_DEPTH** (line 107)
- **ZYNQ_QSPI_GPIO_OFFSET** (line 36)
- **ZYNQ_QSPI_IDIS_OFFSET** (line 24)
- **ZYNQ_QSPI_IEN_OFFSET** (line 23)
- **ZYNQ_QSPI_IMASK_OFFSET** (line 25)
- **ZYNQ_QSPI_IXR_ALL_MASK** (line 78)
- **ZYNQ_QSPI_IXR_RXF_FULL_MASK** (line 76)
- **ZYNQ_QSPI_IXR_RXNEMTY_MASK** (line 75)
- **ZYNQ_QSPI_IXR_RXTX_MASK** (line 84)
- **ZYNQ_QSPI_IXR_RX_OVERFLOW_MASK** (line 72)
- **ZYNQ_QSPI_IXR_TXFULL_MASK** (line 74)
- **ZYNQ_QSPI_IXR_TXF_UNDRFLOW_MASK** (line 77)
- **ZYNQ_QSPI_IXR_TXNFULL_MASK** (line 73)
- **ZYNQ_QSPI_LCFG_DUMMY_SHIFT** (line 104)
- **ZYNQ_QSPI_LCFG_SEP_BUS** (line 101)
- **ZYNQ_QSPI_LCFG_TWO_MEM** (line 100)
- **ZYNQ_QSPI_LCFG_U_PAGE** (line 102)
- **ZYNQ_QSPI_LINEAR_CFG_OFFSET** (line 37)
- **ZYNQ_QSPI_MAX_NUM_CS** (line 118)
- **ZYNQ_QSPI_MODEBITS** (line 115)
- **ZYNQ_QSPI_MOD_ID_OFFSET** (line 38)
- **ZYNQ_QSPI_RXD_OFFSET** (line 32)
- **ZYNQ_QSPI_RX_THRESHOLD** (line 108)
- **ZYNQ_QSPI_RX_THRESH_OFFSET** (line 35)
- **ZYNQ_QSPI_SIC_OFFSET** (line 33)
- **ZYNQ_QSPI_STATUS_OFFSET** (line 22)
- **ZYNQ_QSPI_TXD_00_00_OFFSET** (line 28)
- **ZYNQ_QSPI_TXD_00_01_OFFSET** (line 29)
- **ZYNQ_QSPI_TXD_00_10_OFFSET** (line 30)
- **ZYNQ_QSPI_TXD_00_11_OFFSET** (line 31)
- **ZYNQ_QSPI_TX_THRESHOLD** (line 109)
- **ZYNQ_QSPI_TX_THRESH_OFFSET** (line 34)
