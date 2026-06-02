# drivers/spi/spi-s3c64xx.c

Subsystem: drivers/spi

## Functions (34)

### s3c64xx_enable_datapath
- Return type: static int
- Signature: s3c64xx_enable_datapath(struct s3c64xx_spi_driver_data * sdd,struct spi_transfer * xfer,int dma_mode)
- Line: 490

### s3c64xx_flush_fifo
- Return type: static void
- Signature: s3c64xx_flush_fifo(struct s3c64xx_spi_driver_data * sdd)
- Line: 229

### s3c64xx_get_target_ctrldata
- Return type: static s3c64xx_spi_csinfo *
- Signature: s3c64xx_get_target_ctrldata(struct spi_device * spi)
- Line: 951

### s3c64xx_iowrite16_32_rep
- Return type: static void
- Signature: s3c64xx_iowrite16_32_rep(volatile void __iomem * addr,const void * buffer,unsigned int count)
- Line: 452

### s3c64xx_iowrite8_32_rep
- Return type: static void
- Signature: s3c64xx_iowrite8_32_rep(volatile void __iomem * addr,const void * buffer,unsigned int count)
- Line: 440

### s3c64xx_iowrite_rep
- Return type: static void
- Signature: s3c64xx_iowrite_rep(const struct s3c64xx_spi_driver_data * sdd,struct spi_transfer * xfer)
- Line: 464

### s3c64xx_prepare_dma
- Return type: static int
- Signature: s3c64xx_prepare_dma(struct s3c64xx_spi_dma_data * dma,struct sg_table * sgt)
- Line: 305

### s3c64xx_spi_can_dma
- Return type: static bool
- Signature: s3c64xx_spi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 428

### s3c64xx_spi_cleanup
- Return type: static void
- Signature: s3c64xx_spi_cleanup(struct spi_device * spi)
- Line: 1067

### s3c64xx_spi_config
- Return type: static int
- Signature: s3c64xx_spi_config(struct s3c64xx_spi_driver_data * sdd)
- Line: 695

### s3c64xx_spi_dmacb
- Return type: static void
- Signature: s3c64xx_spi_dmacb(void * data)
- Line: 277

### s3c64xx_spi_get_port_config
- Return type: static const struct s3c64xx_spi_port_config *
- Signature: s3c64xx_spi_get_port_config(struct platform_device * pdev)
- Line: 1194

### s3c64xx_spi_hwinit
- Return type: static void
- Signature: s3c64xx_spi_hwinit(struct s3c64xx_spi_driver_data * sdd)
- Line: 1118

### s3c64xx_spi_irq
- Return type: static irqreturn_t
- Signature: s3c64xx_spi_irq(int irq,void * data)
- Line: 1078

### s3c64xx_spi_max_transfer_size
- Return type: static size_t
- Signature: s3c64xx_spi_max_transfer_size(struct spi_device * spi)
- Line: 791

### s3c64xx_spi_parse_dt
- Return type: static s3c64xx_spi_info *
- Signature: s3c64xx_spi_parse_dt(struct device * dev)
- Line: 1159

### s3c64xx_spi_parse_dt
- Return type: static s3c64xx_spi_info *
- Signature: s3c64xx_spi_parse_dt(struct device * dev)
- Line: 1188

### s3c64xx_spi_prepare_message
- Return type: static int
- Signature: s3c64xx_spi_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 774

### s3c64xx_spi_prepare_transfer
- Return type: static int
- Signature: s3c64xx_spi_prepare_transfer(struct spi_controller * spi)
- Line: 380

### s3c64xx_spi_probe
- Return type: static int
- Signature: s3c64xx_spi_probe(struct platform_device * pdev)
- Line: 1246

### s3c64xx_spi_remove
- Return type: static void
- Signature: s3c64xx_spi_remove(struct platform_device * pdev)
- Line: 1395

### s3c64xx_spi_resume
- Return type: static int
- Signature: s3c64xx_spi_resume(struct device * dev)
- Line: 1431

### s3c64xx_spi_runtime_resume
- Return type: static int
- Signature: s3c64xx_spi_runtime_resume(struct device * dev)
- Line: 1462

### s3c64xx_spi_runtime_suspend
- Return type: static int
- Signature: s3c64xx_spi_runtime_suspend(struct device * dev)
- Line: 1450

### s3c64xx_spi_set_cs
- Return type: static void
- Signature: s3c64xx_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 355

### s3c64xx_spi_set_fifomask
- Return type: static void
- Signature: s3c64xx_spi_set_fifomask(struct s3c64xx_spi_driver_data * sdd)
- Line: 1229

### s3c64xx_spi_set_port_id
- Return type: static int
- Signature: s3c64xx_spi_set_port_id(struct platform_device * pdev,struct s3c64xx_spi_driver_data * sdd)
- Line: 1204

### s3c64xx_spi_setup
- Return type: static int
- Signature: s3c64xx_spi_setup(struct spi_device * spi)
- Line: 986

### s3c64xx_spi_suspend
- Return type: static int
- Signature: s3c64xx_spi_suspend(struct device * dev)
- Line: 1412

### s3c64xx_spi_transfer_one
- Return type: static int
- Signature: s3c64xx_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 798

### s3c64xx_spi_unprepare_transfer
- Return type: static int
- Signature: s3c64xx_spi_unprepare_transfer(struct spi_controller * spi)
- Line: 410

### s3c64xx_spi_wait_for_timeout
- Return type: static u32
- Signature: s3c64xx_spi_wait_for_timeout(struct s3c64xx_spi_driver_data * sdd,int timeout_ms)
- Line: 553

### s3c64xx_wait_for_dma
- Return type: static int
- Signature: s3c64xx_wait_for_dma(struct s3c64xx_spi_driver_data * sdd,struct spi_transfer * xfer)
- Line: 572

### s3c64xx_wait_for_pio
- Return type: static int
- Signature: s3c64xx_wait_for_pio(struct s3c64xx_spi_driver_data * sdd,struct spi_transfer * xfer,bool use_irq)
- Line: 616

## Structs (3)

### s3c64xx_spi_dma_data
- Line: 132
- Members:
  - ch: dma_chan *
  - cookie: dma_cookie_t
  - direction: dma_transfer_direction
  - fifo_lvl_mask: int[]
  - rx_lvl_offset: int
  - fifo_depth: unsigned int
  - rx_fifomask: u32
  - tx_fifomask: u32
  - tx_st_done: int
  - quirks: int
  - clk_div: int
  - high_speed: bool
  - clk_from_cmu: bool
  - clk_ioclk: bool
  - has_loopback: bool
  - use_32bit_io: bool
  - regs: void __iomem *
  - clk: clk *
  - src_clk: clk *
  - ioclk: clk *
  - pdev: platform_device *
  - host: spi_controller *
  - cntrlr_info: s3c64xx_spi_info *
  - lock: spinlock_t
  - sfr_start: unsigned long
  - xfer_completion: completion
  - state: unsigned
  - cur_bpw: unsigned
  - cur_mode: unsigned
  - cur_speed: unsigned
  - rx_dma: s3c64xx_spi_dma_data
  - tx_dma: s3c64xx_spi_dma_data
  - port_conf: const struct s3c64xx_spi_port_config *
  - port_id: unsigned int
  - fifo_depth: unsigned int
  - rx_fifomask: u32
  - tx_fifomask: u32

### s3c64xx_spi_driver_data
- Line: 206
- Members:
  - ch: dma_chan *
  - cookie: dma_cookie_t
  - direction: dma_transfer_direction
  - fifo_lvl_mask: int[]
  - rx_lvl_offset: int
  - fifo_depth: unsigned int
  - rx_fifomask: u32
  - tx_fifomask: u32
  - tx_st_done: int
  - quirks: int
  - clk_div: int
  - high_speed: bool
  - clk_from_cmu: bool
  - clk_ioclk: bool
  - has_loopback: bool
  - use_32bit_io: bool
  - regs: void __iomem *
  - clk: clk *
  - src_clk: clk *
  - ioclk: clk *
  - pdev: platform_device *
  - host: spi_controller *
  - cntrlr_info: s3c64xx_spi_info *
  - lock: spinlock_t
  - sfr_start: unsigned long
  - xfer_completion: completion
  - state: unsigned
  - cur_bpw: unsigned
  - cur_mode: unsigned
  - cur_speed: unsigned
  - rx_dma: s3c64xx_spi_dma_data
  - tx_dma: s3c64xx_spi_dma_data
  - port_conf: const struct s3c64xx_spi_port_config *
  - port_id: unsigned int
  - fifo_depth: unsigned int
  - rx_fifomask: u32
  - tx_fifomask: u32

### s3c64xx_spi_port_config
- Line: 164
- Members:
  - ch: dma_chan *
  - cookie: dma_cookie_t
  - direction: dma_transfer_direction
  - fifo_lvl_mask: int[]
  - rx_lvl_offset: int
  - fifo_depth: unsigned int
  - rx_fifomask: u32
  - tx_fifomask: u32
  - tx_st_done: int
  - quirks: int
  - clk_div: int
  - high_speed: bool
  - clk_from_cmu: bool
  - clk_ioclk: bool
  - has_loopback: bool
  - use_32bit_io: bool
  - regs: void __iomem *
  - clk: clk *
  - src_clk: clk *
  - ioclk: clk *
  - pdev: platform_device *
  - host: spi_controller *
  - cntrlr_info: s3c64xx_spi_info *
  - lock: spinlock_t
  - sfr_start: unsigned long
  - xfer_completion: completion
  - state: unsigned
  - cur_bpw: unsigned
  - cur_mode: unsigned
  - cur_speed: unsigned
  - rx_dma: s3c64xx_spi_dma_data
  - tx_dma: s3c64xx_spi_dma_data
  - port_conf: const struct s3c64xx_spi_port_config *
  - port_id: unsigned int
  - fifo_depth: unsigned int
  - rx_fifomask: u32
  - tx_fifomask: u32

## Variables (13)

- static **exynos4_spi_port_config** : const struct s3c64xx_spi_port_config (line 1524)
- static **exynos5433_spi_port_config** : const struct s3c64xx_spi_port_config (line 1548)
- static **exynos7_spi_port_config** : const struct s3c64xx_spi_port_config (line 1536)
- static **exynos850_spi_port_config** : const struct s3c64xx_spi_port_config (line 1561)
- static **exynosautov9_spi_port_config** : const struct s3c64xx_spi_port_config (line 1573)
- static **fsd_spi_port_config** : const struct s3c64xx_spi_port_config (line 1588)
- static **gs101_spi_port_config** : const struct s3c64xx_spi_port_config (line 1601)
- static **s3c6410_spi_port_config** : const struct s3c64xx_spi_port_config (line 1505)
- static **s3c64xx_spi_driver** : platform_driver (line 1655)
- static **s3c64xx_spi_driver_ids** : const struct platform_device_id[] (line 1614)
- static **s3c64xx_spi_dt_match** : const struct of_device_id[] (line 1623)
- static **s3c64xx_spi_pm** : const struct dev_pm_ops (line 1499)
- static **s5pv210_spi_port_config** : const struct s3c64xx_spi_port_config (line 1514)

## Macros (88)

- **AUTOSUSPEND_TIMEOUT** (line 25)
- **FIFO_DEPTH**(i) (line 119)
- **FIFO_LVL_MASK**(i) (line 112)
- **MAX_SPI_PORTS** (line 23)
- **RXBUSY** (line 129)
- **RX_FIFO_LVL**(v,sdd) (line 117)
- **S3C64XX_SPI_CH_CFG** (line 29)
- **S3C64XX_SPI_CH_HS_EN** (line 42)
- **S3C64XX_SPI_CH_RXCH_ON** (line 47)
- **S3C64XX_SPI_CH_SLAVE** (line 44)
- **S3C64XX_SPI_CH_SW_RST** (line 43)
- **S3C64XX_SPI_CH_TXCH_ON** (line 48)
- **S3C64XX_SPI_CLKSEL_SRCMSK** (line 50)
- **S3C64XX_SPI_CLKSEL_SRCSHFT** (line 51)
- **S3C64XX_SPI_CLK_CFG** (line 30)
- **S3C64XX_SPI_CPHA_B** (line 46)
- **S3C64XX_SPI_CPOL_L** (line 45)
- **S3C64XX_SPI_CS_AUTO** (line 71)
- **S3C64XX_SPI_CS_NSC_CNT_2** (line 70)
- **S3C64XX_SPI_CS_REG** (line 32)
- **S3C64XX_SPI_CS_SIG_INACT** (line 72)
- **S3C64XX_SPI_ENCLK_ENABLE** (line 52)
- **S3C64XX_SPI_FBCLK_MSK** (line 110)
- **S3C64XX_SPI_FB_CLK** (line 40)
- **S3C64XX_SPI_INT_EN** (line 33)
- **S3C64XX_SPI_INT_RX_FIFORDY_EN** (line 79)
- **S3C64XX_SPI_INT_RX_OVERRUN_EN** (line 75)
- **S3C64XX_SPI_INT_RX_UNDERRUN_EN** (line 76)
- **S3C64XX_SPI_INT_TRAILING_EN** (line 74)
- **S3C64XX_SPI_INT_TX_FIFORDY_EN** (line 80)
- **S3C64XX_SPI_INT_TX_OVERRUN_EN** (line 77)
- **S3C64XX_SPI_INT_TX_UNDERRUN_EN** (line 78)
- **S3C64XX_SPI_MAX_TRAILCNT** (line 121)
- **S3C64XX_SPI_MODE_4BURST** (line 68)
- **S3C64XX_SPI_MODE_BUS_TSZ_BYTE** (line 59)
- **S3C64XX_SPI_MODE_BUS_TSZ_HALFWORD** (line 60)
- **S3C64XX_SPI_MODE_BUS_TSZ_MASK** (line 62)
- **S3C64XX_SPI_MODE_BUS_TSZ_WORD** (line 61)
- **S3C64XX_SPI_MODE_CFG** (line 31)
- **S3C64XX_SPI_MODE_CH_TSZ_BYTE** (line 55)
- **S3C64XX_SPI_MODE_CH_TSZ_HALFWORD** (line 56)
- **S3C64XX_SPI_MODE_CH_TSZ_MASK** (line 58)
- **S3C64XX_SPI_MODE_CH_TSZ_WORD** (line 57)
- **S3C64XX_SPI_MODE_RXDMA_ON** (line 66)
- **S3C64XX_SPI_MODE_RX_RDY_LVL** (line 63)
- **S3C64XX_SPI_MODE_RX_RDY_LVL_SHIFT** (line 64)
- **S3C64XX_SPI_MODE_SELF_LOOPBACK** (line 65)
- **S3C64XX_SPI_MODE_TXDMA_ON** (line 67)
- **S3C64XX_SPI_PACKET_CNT** (line 37)
- **S3C64XX_SPI_PACKET_CNT_EN** (line 92)
- **S3C64XX_SPI_PACKET_CNT_MASK** (line 93)
- **S3C64XX_SPI_PENDING_CLR** (line 38)
- **S3C64XX_SPI_PND_RX_OVERRUN_CLR** (line 98)
- **S3C64XX_SPI_PND_RX_UNDERRUN_CLR** (line 97)
- **S3C64XX_SPI_PND_TRAILING_CLR** (line 99)
- **S3C64XX_SPI_PND_TX_OVERRUN_CLR** (line 96)
- **S3C64XX_SPI_PND_TX_UNDERRUN_CLR** (line 95)
- **S3C64XX_SPI_POLLING_SIZE** (line 124)
- **S3C64XX_SPI_PSR_MASK** (line 53)
- **S3C64XX_SPI_QUIRK_CS_AUTO** (line 24)
- **S3C64XX_SPI_RX_DATA** (line 36)
- **S3C64XX_SPI_STATUS** (line 34)
- **S3C64XX_SPI_ST_RX_FIFORDY** (line 89)
- **S3C64XX_SPI_ST_RX_FIFO_RDY_V2** (line 82)
- **S3C64XX_SPI_ST_RX_OVERRUN_ERR** (line 85)
- **S3C64XX_SPI_ST_RX_UNDERRUN_ERR** (line 86)
- **S3C64XX_SPI_ST_TX_DONE**(v,i) (line 113)
- **S3C64XX_SPI_ST_TX_FIFORDY** (line 90)
- **S3C64XX_SPI_ST_TX_FIFO_LVL_SHIFT** (line 84)
- **S3C64XX_SPI_ST_TX_FIFO_RDY_V2** (line 83)
- **S3C64XX_SPI_ST_TX_OVERRUN_ERR** (line 87)
- **S3C64XX_SPI_ST_TX_UNDERRUN_ERR** (line 88)
- **S3C64XX_SPI_SWAP_CFG** (line 39)
- **S3C64XX_SPI_SWAP_RX_BIT** (line 103)
- **S3C64XX_SPI_SWAP_RX_BYTE** (line 102)
- **S3C64XX_SPI_SWAP_RX_EN** (line 104)
- **S3C64XX_SPI_SWAP_RX_HALF_WORD** (line 101)
- **S3C64XX_SPI_SWAP_TX_BIT** (line 107)
- **S3C64XX_SPI_SWAP_TX_BYTE** (line 106)
- **S3C64XX_SPI_SWAP_TX_EN** (line 108)
- **S3C64XX_SPI_SWAP_TX_HALF_WORD** (line 105)
- **S3C64XX_SPI_TRAILCNT_OFF** (line 122)
- **S3C64XX_SPI_TX_DATA** (line 35)
- **TXBUSY** (line 130)
- **TX_FIFO_LVL**(v,sdd) (line 115)
- **XFER_DMAADDR_INVALID** (line 772)
- **is_polling**(x) (line 127)
- **msecs_to_loops**(t) (line 126)
