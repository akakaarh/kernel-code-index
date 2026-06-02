# drivers/spi/spi-sprd.c

Subsystem: drivers/spi

## Functions (40)

### sprd_spi_can_dma
- Return type: static bool
- Signature: sprd_spi_can_dma(struct spi_controller * sctlr,struct spi_device * spi,struct spi_transfer * t)
- Line: 889

### sprd_spi_chipselect
- Return type: static void
- Signature: sprd_spi_chipselect(struct spi_device * sdev,bool cs)
- Line: 290

### sprd_spi_clk_init
- Return type: static int
- Signature: sprd_spi_clk_init(struct platform_device * pdev,struct sprd_spi * ss)
- Line: 859

### sprd_spi_dma_enable
- Return type: static void
- Signature: sprd_spi_dma_enable(struct sprd_spi * ss,bool enable)
- Line: 475

### sprd_spi_dma_init
- Return type: static int
- Signature: sprd_spi_dma_init(struct platform_device * pdev,struct sprd_spi * ss)
- Line: 897

### sprd_spi_dma_release
- Return type: static void
- Signature: sprd_spi_dma_release(struct sprd_spi * ss)
- Line: 569

### sprd_spi_dma_request
- Return type: static int
- Signature: sprd_spi_dma_request(struct sprd_spi * ss)
- Line: 552

### sprd_spi_dma_rx_config
- Return type: static int
- Signature: sprd_spi_dma_rx_config(struct sprd_spi * ss,struct spi_transfer * t)
- Line: 516

### sprd_spi_dma_submit
- Return type: static int
- Signature: sprd_spi_dma_submit(struct dma_chan * dma_chan,struct dma_slave_config * c,struct sg_table * sg,enum dma_transfer_direction dir)
- Line: 487

### sprd_spi_dma_tx_config
- Return type: static int
- Signature: sprd_spi_dma_tx_config(struct sprd_spi * ss,struct spi_transfer * t)
- Line: 534

### sprd_spi_dma_txrx_bufs
- Return type: static int
- Signature: sprd_spi_dma_txrx_bufs(struct spi_device * sdev,struct spi_transfer * t)
- Line: 578

### sprd_spi_enter_idle
- Return type: static void
- Signature: sprd_spi_enter_idle(struct sprd_spi * ss)
- Line: 246

### sprd_spi_handle_irq
- Return type: static irqreturn_t
- Signature: sprd_spi_handle_irq(int irq,void * data)
- Line: 814

### sprd_spi_init_hw
- Return type: static int
- Signature: sprd_spi_init_hw(struct sprd_spi * ss,struct spi_transfer * t)
- Line: 664

### sprd_spi_irq_disable
- Return type: static void
- Signature: sprd_spi_irq_disable(struct sprd_spi * ss)
- Line: 470

### sprd_spi_irq_enable
- Return type: static void
- Signature: sprd_spi_irq_enable(struct sprd_spi * ss)
- Line: 456

### sprd_spi_irq_init
- Return type: static int
- Signature: sprd_spi_irq_init(struct platform_device * pdev,struct sprd_spi * ss)
- Line: 842

### sprd_spi_probe
- Return type: static int
- Signature: sprd_spi_probe(struct platform_device * pdev)
- Line: 918

### sprd_spi_read_bufs_u16
- Return type: static int
- Signature: sprd_spi_read_bufs_u16(struct sprd_spi * ss,u32 len)
- Line: 377

### sprd_spi_read_bufs_u32
- Return type: static int
- Signature: sprd_spi_read_bufs_u32(struct sprd_spi * ss,u32 len)
- Line: 389

### sprd_spi_read_bufs_u8
- Return type: static int
- Signature: sprd_spi_read_bufs_u8(struct sprd_spi * ss,u32 len)
- Line: 365

### sprd_spi_remove
- Return type: static void
- Signature: sprd_spi_remove(struct platform_device * pdev)
- Line: 1002

### sprd_spi_runtime_resume
- Return type: static int __maybe_unused
- Signature: sprd_spi_runtime_resume(struct device * dev)
- Line: 1040

### sprd_spi_runtime_suspend
- Return type: static int __maybe_unused
- Signature: sprd_spi_runtime_suspend(struct device * dev)
- Line: 1027

### sprd_spi_rx_req
- Return type: static void
- Signature: sprd_spi_rx_req(struct sprd_spi * ss)
- Line: 241

### sprd_spi_set_rx_length
- Return type: static void
- Signature: sprd_spi_set_rx_length(struct sprd_spi * ss,u32 length)
- Line: 277

### sprd_spi_set_speed
- Return type: static void
- Signature: sprd_spi_set_speed(struct sprd_spi * ss,u32 speed_hz)
- Line: 651

### sprd_spi_set_transfer_bits
- Return type: static void
- Signature: sprd_spi_set_transfer_bits(struct sprd_spi * ss,u32 bits)
- Line: 254

### sprd_spi_set_tx_length
- Return type: static void
- Signature: sprd_spi_set_tx_length(struct sprd_spi * ss,u32 length)
- Line: 264

### sprd_spi_setup_transfer
- Return type: static int
- Signature: sprd_spi_setup_transfer(struct spi_device * sdev,struct spi_transfer * t)
- Line: 714

### sprd_spi_transfer_max_timeout
- Return type: static u32
- Signature: sprd_spi_transfer_max_timeout(struct sprd_spi * ss,struct spi_transfer * t)
- Line: 172

### sprd_spi_transfer_one
- Return type: static int
- Signature: sprd_spi_transfer_one(struct spi_controller * sctlr,struct spi_device * sdev,struct spi_transfer * t)
- Line: 788

### sprd_spi_tx_req
- Return type: static void
- Signature: sprd_spi_tx_req(struct sprd_spi * ss)
- Line: 236

### sprd_spi_txrx_bufs
- Return type: static int
- Signature: sprd_spi_txrx_bufs(struct spi_device * sdev,struct spi_transfer * t)
- Line: 401

### sprd_spi_wait_for_rx_end
- Return type: static int
- Signature: sprd_spi_wait_for_rx_end(struct sprd_spi * ss,struct spi_transfer * t)
- Line: 218

### sprd_spi_wait_for_tx_end
- Return type: static int
- Signature: sprd_spi_wait_for_tx_end(struct sprd_spi * ss,struct spi_transfer * t)
- Line: 193

### sprd_spi_write_bufs_u16
- Return type: static int
- Signature: sprd_spi_write_bufs_u16(struct sprd_spi * ss,u32 len)
- Line: 341

### sprd_spi_write_bufs_u32
- Return type: static int
- Signature: sprd_spi_write_bufs_u32(struct sprd_spi * ss,u32 len)
- Line: 353

### sprd_spi_write_bufs_u8
- Return type: static int
- Signature: sprd_spi_write_bufs_u8(struct sprd_spi * ss,u32 len)
- Line: 329

### sprd_spi_write_only_receive
- Return type: static int
- Signature: sprd_spi_write_only_receive(struct sprd_spi * ss,u32 len)
- Line: 307

## Structs (2)

### sprd_spi
- Line: 150
- Members:
  - enable: bool
  - dma_chan: dma_chan * []
  - width: dma_slave_buswidth
  - fragmens_len: u32
  - rx_len: u32
  - base: void __iomem *
  - phy_base: phys_addr_t
  - dev: device *
  - clk: clk *
  - irq: int
  - src_clk: u32
  - hw_mode: u32
  - trans_len: u32
  - trans_mode: u32
  - word_delay: u32
  - hw_speed_hz: u32
  - len: u32
  - status: int
  - dma: sprd_spi_dma
  - xfer_completion: completion
  - tx_buf: const void *
  - rx_buf: void *
  - read_bufs: int (*)(struct sprd_spi * ss,u32 len)
  - write_bufs: int (*)(struct sprd_spi * ss,u32 len)

### sprd_spi_dma
- Line: 142
- Members:
  - enable: bool
  - dma_chan: dma_chan * []
  - width: dma_slave_buswidth
  - fragmens_len: u32
  - rx_len: u32
  - base: void __iomem *
  - phy_base: phys_addr_t
  - dev: device *
  - clk: clk *
  - irq: int
  - src_clk: u32
  - hw_mode: u32
  - trans_len: u32
  - trans_mode: u32
  - word_delay: u32
  - hw_speed_hz: u32
  - len: u32
  - status: int
  - dma: sprd_spi_dma
  - xfer_completion: completion
  - tx_buf: const void *
  - rx_buf: void *
  - read_bufs: int (*)(struct sprd_spi * ss,u32 len)
  - write_bufs: int (*)(struct sprd_spi * ss,u32 len)

## Enums (1)

### sprd_spi_dma_channel
- Line: 136

## Variables (3)

- static **sprd_spi_driver** : platform_driver (line 1071)
- static **sprd_spi_of_match** : const struct of_device_id[] (line 1065)
- static **sprd_spi_pm_ops** : const struct dev_pm_ops (line 1060)

## Macros (79)

- **SPRD_SPI_3WIRE_MODE** (line 105)
- **SPRD_SPI_4WIRE_MODE** (line 106)
- **SPRD_SPI_AUTOSUSPEND_DELAY** (line 133)
- **SPRD_SPI_CHIP_CS_NUM** (line 129)
- **SPRD_SPI_CHNL_LEN** (line 130)
- **SPRD_SPI_CHNL_LEN_MASK** (line 54)
- **SPRD_SPI_CLKD** (line 20)
- **SPRD_SPI_CS0_VALID** (line 56)
- **SPRD_SPI_CSN_MASK** (line 55)
- **SPRD_SPI_CTL0** (line 21)
- **SPRD_SPI_CTL1** (line 22)
- **SPRD_SPI_CTL10** (line 42)
- **SPRD_SPI_CTL11** (line 43)
- **SPRD_SPI_CTL12** (line 44)
- **SPRD_SPI_CTL2** (line 23)
- **SPRD_SPI_CTL3** (line 24)
- **SPRD_SPI_CTL4** (line 25)
- **SPRD_SPI_CTL5** (line 26)
- **SPRD_SPI_CTL6** (line 35)
- **SPRD_SPI_CTL7** (line 38)
- **SPRD_SPI_CTL8** (line 40)
- **SPRD_SPI_CTL9** (line 41)
- **SPRD_SPI_DATA_LINE2_EN** (line 102)
- **SPRD_SPI_DEFAULT_SOURCE** (line 131)
- **SPRD_SPI_DMA_EN** (line 83)
- **SPRD_SPI_DMA_STEP** (line 134)
- **SPRD_SPI_DSP_WAIT** (line 33)
- **SPRD_SPI_FIFO_RST** (line 37)
- **SPRD_SPI_FIFO_SIZE** (line 128)
- **SPRD_SPI_INT_CLR** (line 28)
- **SPRD_SPI_INT_EN** (line 27)
- **SPRD_SPI_INT_MASK_STS** (line 30)
- **SPRD_SPI_INT_RAW_STS** (line 29)
- **SPRD_SPI_MASK_RX_END** (line 71)
- **SPRD_SPI_MASK_TX_END** (line 72)
- **SPRD_SPI_MAX_DELAY_CYCLE** (line 126)
- **SPRD_SPI_MAX_SPEED_HZ** (line 132)
- **SPRD_SPI_MIN_DELAY_CYCLE** (line 125)
- **SPRD_SPI_MODE_MASK** (line 103)
- **SPRD_SPI_MODE_OFFSET** (line 104)
- **SPRD_SPI_NG_RX** (line 53)
- **SPRD_SPI_NG_TX** (line 52)
- **SPRD_SPI_ONLY_RECV_MASK** (line 87)
- **SPRD_SPI_RTX_MD_MASK** (line 80)
- **SPRD_SPI_RX_END_CLR** (line 68)
- **SPRD_SPI_RX_END_INT_CLR** (line 90)
- **SPRD_SPI_RX_END_INT_EN** (line 60)
- **SPRD_SPI_RX_END_IRQ** (line 94)
- **SPRD_SPI_RX_END_RAW** (line 64)
- **SPRD_SPI_RX_LEN_H_MASK** (line 118)
- **SPRD_SPI_RX_LEN_H_OFFSET** (line 119)
- **SPRD_SPI_RX_LEN_L_MASK** (line 122)
- **SPRD_SPI_RX_MAX_LEN_MASK** (line 117)
- **SPRD_SPI_RX_MODE** (line 78)
- **SPRD_SPI_SCK_REV** (line 51)
- **SPRD_SPI_START_RX** (line 86)
- **SPRD_SPI_STS1** (line 31)
- **SPRD_SPI_STS2** (line 32)
- **SPRD_SPI_STS3** (line 34)
- **SPRD_SPI_STS4** (line 36)
- **SPRD_SPI_STS5** (line 39)
- **SPRD_SPI_STS6** (line 45)
- **SPRD_SPI_STS7** (line 46)
- **SPRD_SPI_STS8** (line 47)
- **SPRD_SPI_STS9** (line 48)
- **SPRD_SPI_SW_RX_REQ** (line 98)
- **SPRD_SPI_SW_TX_REQ** (line 99)
- **SPRD_SPI_TXD** (line 19)
- **SPRD_SPI_TX_BUSY** (line 75)
- **SPRD_SPI_TX_END_CLR** (line 67)
- **SPRD_SPI_TX_END_INT_CLR** (line 91)
- **SPRD_SPI_TX_END_INT_EN** (line 59)
- **SPRD_SPI_TX_END_IRQ** (line 95)
- **SPRD_SPI_TX_END_RAW** (line 63)
- **SPRD_SPI_TX_LEN_H_MASK** (line 110)
- **SPRD_SPI_TX_LEN_H_OFFSET** (line 111)
- **SPRD_SPI_TX_LEN_L_MASK** (line 114)
- **SPRD_SPI_TX_MAX_LEN_MASK** (line 109)
- **SPRD_SPI_TX_MODE** (line 79)
