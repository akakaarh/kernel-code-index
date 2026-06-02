# drivers/spi/spi-amlogic-spisg.c

Subsystem: drivers/spi

## Functions (21)

### aml_spisg_can_dma
- Return type: static bool
- Signature: aml_spisg_can_dma(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 218

### aml_spisg_cleanup
- Return type: static void
- Signature: aml_spisg_cleanup(struct spi_device * spi)
- Line: 624

### aml_spisg_cleanup_transfer
- Return type: static void
- Signature: aml_spisg_cleanup_transfer(struct spisg_device * spisg,struct spi_transfer * xfer,struct spisg_descriptor * desc,struct spisg_descriptor_extra * exdesc)
- Line: 376

### aml_spisg_clk_init
- Return type: static int
- Signature: aml_spisg_clk_init(struct spisg_device * spisg,void __iomem * base)
- Line: 640

### aml_spisg_irq
- Return type: static irqreturn_t
- Signature: aml_spisg_irq(int irq,void * data)
- Line: 456

### aml_spisg_pending
- Return type: static void
- Signature: aml_spisg_pending(struct spisg_device * spisg,dma_addr_t desc_paddr,bool trig,bool irq_en)
- Line: 425

### aml_spisg_prepare_message
- Return type: static int
- Signature: aml_spisg_prepare_message(struct spi_controller * ctlr,struct spi_message * message)
- Line: 591

### aml_spisg_probe
- Return type: static int
- Signature: aml_spisg_probe(struct platform_device * pdev)
- Line: 716

### aml_spisg_remove
- Return type: static void
- Signature: aml_spisg_remove(struct platform_device * pdev)
- Line: 821

### aml_spisg_sem_down_read
- Return type: static u32
- Signature: aml_spisg_sem_down_read(struct spisg_device * spisg)
- Line: 181

### aml_spisg_sem_up_write
- Return type: static void
- Signature: aml_spisg_sem_up_write(struct spisg_device * spisg)
- Line: 192

### aml_spisg_set_speed
- Return type: static int
- Signature: aml_spisg_set_speed(struct spisg_device * spisg,uint speed_hz)
- Line: 197

### aml_spisg_setup
- Return type: static int
- Signature: aml_spisg_setup(struct spi_device * spi)
- Line: 616

### aml_spisg_setup_null_desc
- Return type: static void
- Signature: aml_spisg_setup_null_desc(struct spisg_device * spisg,struct spisg_descriptor * desc,u32 n_sclk)
- Line: 410

### aml_spisg_setup_transfer
- Return type: static int
- Signature: aml_spisg_setup_transfer(struct spisg_device * spisg,struct spi_transfer * xfer,struct spisg_descriptor * desc,struct spisg_descriptor_extra * exdesc)
- Line: 248

### aml_spisg_sg_xlate
- Return type: static void
- Signature: aml_spisg_sg_xlate(struct sg_table * sgt,struct spisg_sg_link * ccsg)
- Line: 225

### aml_spisg_target_abort
- Return type: static int
- Signature: aml_spisg_target_abort(struct spi_controller * ctlr)
- Line: 629

### aml_spisg_transfer_one_message
- Return type: static int
- Signature: aml_spisg_transfer_one_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 482

### spi_delay_to_sclk
- Return type: static int
- Signature: spi_delay_to_sclk(u32 slck_speed_hz,struct spi_delay * delay)
- Line: 164

### spisg_resume_runtime
- Return type: static int
- Signature: spisg_resume_runtime(struct device * dev)
- Line: 845

### spisg_suspend_runtime
- Return type: static int
- Signature: spisg_suspend_runtime(struct device * dev)
- Line: 834

## Structs (4)

### spisg_descriptor
- Line: 132
- Members:
  - addr: u32
  - addr1: u32
  - cfg_start: u32
  - cfg_bus: u32
  - tx_paddr: u64
  - rx_paddr: u64
  - tx_ccsg: spisg_sg_link *
  - rx_ccsg: spisg_sg_link *
  - tx_ccsg_len: int
  - rx_ccsg_len: int
  - controller: spi_controller *
  - pdev: platform_device *
  - map: regmap *
  - core: clk *
  - pclk: clk *
  - sclk: clk *
  - tbl: clk_div_table *
  - completion: completion
  - status: u32
  - speed_hz: u32
  - effective_speed_hz: u32
  - bytes_per_word: u32
  - cfg_spi: u32
  - cfg_start: u32
  - cfg_bus: u32

### spisg_descriptor_extra
- Line: 139
- Members:
  - addr: u32
  - addr1: u32
  - cfg_start: u32
  - cfg_bus: u32
  - tx_paddr: u64
  - rx_paddr: u64
  - tx_ccsg: spisg_sg_link *
  - rx_ccsg: spisg_sg_link *
  - tx_ccsg_len: int
  - rx_ccsg_len: int
  - controller: spi_controller *
  - pdev: platform_device *
  - map: regmap *
  - core: clk *
  - pclk: clk *
  - sclk: clk *
  - tbl: clk_div_table *
  - completion: completion
  - status: u32
  - speed_hz: u32
  - effective_speed_hz: u32
  - bytes_per_word: u32
  - cfg_spi: u32
  - cfg_start: u32
  - cfg_bus: u32

### spisg_device
- Line: 146
- Members:
  - addr: u32
  - addr1: u32
  - cfg_start: u32
  - cfg_bus: u32
  - tx_paddr: u64
  - rx_paddr: u64
  - tx_ccsg: spisg_sg_link *
  - rx_ccsg: spisg_sg_link *
  - tx_ccsg_len: int
  - rx_ccsg_len: int
  - controller: spi_controller *
  - pdev: platform_device *
  - map: regmap *
  - core: clk *
  - pclk: clk *
  - sclk: clk *
  - tbl: clk_div_table *
  - completion: completion
  - status: u32
  - speed_hz: u32
  - effective_speed_hz: u32
  - bytes_per_word: u32
  - cfg_spi: u32
  - cfg_start: u32
  - cfg_bus: u32

### spisg_sg_link
- Line: 121
- Members:
  - addr: u32
  - addr1: u32
  - cfg_start: u32
  - cfg_bus: u32
  - tx_paddr: u64
  - rx_paddr: u64
  - tx_ccsg: spisg_sg_link *
  - rx_ccsg: spisg_sg_link *
  - tx_ccsg_len: int
  - rx_ccsg_len: int
  - controller: spi_controller *
  - pdev: platform_device *
  - map: regmap *
  - core: clk *
  - pclk: clk *
  - sclk: clk *
  - tbl: clk_div_table *
  - completion: completion
  - status: u32
  - speed_hz: u32
  - effective_speed_hz: u32
  - bytes_per_word: u32
  - cfg_spi: u32
  - cfg_start: u32
  - cfg_bus: u32

## Variables (4)

- static **amlogic_spisg_driver** : platform_driver (line 870)
- static **amlogic_spisg_of_match** : const struct of_device_id[] (line 861)
- static **amlogic_spisg_pm_ops** : const struct dev_pm_ops (line 856)
- static **nbits_to_lane** : int[] (line 240)

## Macros (84)

- **CFG_BLOCK_NUM** (line 42)
- **CFG_BLOCK_SIZE** (line 43)
- **CFG_BUS64_EN** (line 31)
- **CFG_B_L_ENDIAN** (line 59)
- **CFG_CLK_DIV** (line 52)
- **CFG_CPHA** (line 65)
- **CFG_CPOL** (line 66)
- **CFG_CS_SETUP** (line 56)
- **CFG_DATA_COMMAND** (line 44)
- **CFG_DC_MODE** (line 60)
- **CFG_DUMMY_CTL** (line 62)
- **CFG_EOC** (line 48)
- **CFG_HALF_DUPLEX** (line 58)
- **CFG_HW_NEG** (line 39)
- **CFG_HW_POS** (line 37)
- **CFG_KEEP_SS** (line 64)
- **CFG_LANE** (line 57)
- **CFG_NULL_CTL** (line 61)
- **CFG_OP_MODE** (line 45)
- **CFG_PEND** (line 49)
- **CFG_READ_TURN** (line 63)
- **CFG_RXD_MODE** (line 46)
- **CFG_RX_TUNING** (line 54)
- **CFG_SFLASH_HD** (line 35)
- **CFG_SFLASH_WP** (line 34)
- **CFG_SLAVE_EN** (line 32)
- **CFG_SLAVE_SELECT** (line 33)
- **CFG_TXD_MODE** (line 47)
- **CFG_TX_TUNING** (line 55)
- **CLK_DIV_WIDTH** (line 53)
- **DIV_NUM** (line 113)
- **IRQ_DESC_CHAIN_DONE** (line 94)
- **IRQ_DESC_DONE** (line 93)
- **IRQ_DESC_ERR** (line 91)
- **IRQ_RCH_DATA_RESP** (line 86)
- **IRQ_RCH_DESC_EOC** (line 83)
- **IRQ_RCH_DESC_INVALID** (line 84)
- **IRQ_RCH_DESC_RESP** (line 85)
- **IRQ_SPI_READY** (line 92)
- **IRQ_WCH_DATA_RESP** (line 90)
- **IRQ_WCH_DESC_EOC** (line 87)
- **IRQ_WCH_DESC_INVALID** (line 88)
- **IRQ_WCH_DESC_RESP** (line 89)
- **LINK_ADDR_ACT** (line 125)
- **LINK_ADDR_EOC** (line 123)
- **LINK_ADDR_IRQ** (line 124)
- **LINK_ADDR_LEN** (line 127)
- **LINK_ADDR_RING** (line 126)
- **LINK_ADDR_VALID** (line 122)
- **LIST_DESC_PENDING** (line 78)
- **SPISG_BLOCK_MAX** (line 98)
- **SPISG_CLK_DIV_MAX** (line 110)
- **SPISG_CLK_DIV_MIN** (line 112)
- **SPISG_DATA_MODE_MEM** (line 107)
- **SPISG_DATA_MODE_NONE** (line 105)
- **SPISG_DATA_MODE_PIO** (line 106)
- **SPISG_DATA_MODE_SG** (line 108)
- **SPISG_DUAL_SPI** (line 118)
- **SPISG_MAX_REG** (line 96)
- **SPISG_OP_MODE_READ** (line 103)
- **SPISG_OP_MODE_READ_STS** (line 101)
- **SPISG_OP_MODE_WRITE** (line 102)
- **SPISG_OP_MODE_WRITE_CMD** (line 100)
- **SPISG_PCLK_RATE_MIN** (line 115)
- **SPISG_QUAD_SPI** (line 119)
- **SPISG_REG_CFG_BUS** (line 51)
- **SPISG_REG_CFG_READY** (line 28)
- **SPISG_REG_CFG_SPI** (line 30)
- **SPISG_REG_CFG_START** (line 41)
- **SPISG_REG_DESC_CURRENT_H** (line 80)
- **SPISG_REG_DESC_CURRENT_L** (line 79)
- **SPISG_REG_DESC_LIST_H** (line 77)
- **SPISG_REG_DESC_LIST_L** (line 76)
- **SPISG_REG_IRQ_ENABLE** (line 82)
- **SPISG_REG_IRQ_STS** (line 81)
- **SPISG_REG_MEM_RX_ADDR_H** (line 75)
- **SPISG_REG_MEM_RX_ADDR_L** (line 74)
- **SPISG_REG_MEM_TX_ADDR_H** (line 73)
- **SPISG_REG_MEM_TX_ADDR_L** (line 72)
- **SPISG_REG_PIO_RX_DATA_H** (line 71)
- **SPISG_REG_PIO_RX_DATA_L** (line 70)
- **SPISG_REG_PIO_TX_DATA_H** (line 69)
- **SPISG_REG_PIO_TX_DATA_L** (line 68)
- **SPISG_SINGLE_SPI** (line 117)
