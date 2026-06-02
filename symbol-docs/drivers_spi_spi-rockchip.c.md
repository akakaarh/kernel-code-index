# drivers/spi/spi-rockchip.c

Subsystem: drivers/spi

## Functions (25)

### get_fifo_len
- Return type: static u32
- Signature: get_fifo_len(struct rockchip_spi * rs)
- Line: 221

### rockchip_spi_calc_burst_size
- Return type: static u32
- Signature: rockchip_spi_calc_burst_size(u32 data_len)
- Line: 437

### rockchip_spi_can_dma
- Return type: static bool
- Signature: rockchip_spi_can_dma(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 713

### rockchip_spi_config
- Return type: static int
- Signature: rockchip_spi_config(struct rockchip_spi * rs,struct spi_device * spi,struct spi_transfer * xfer,bool use_dma,bool target_mode)
- Line: 529

### rockchip_spi_dma_rxcb
- Return type: static void
- Signature: rockchip_spi_dma_rxcb(void * data)
- Line: 405

### rockchip_spi_dma_txcb
- Return type: static void
- Signature: rockchip_spi_dma_txcb(void * data)
- Line: 421

### rockchip_spi_handle_err
- Return type: static void
- Signature: rockchip_spi_handle_err(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 277

### rockchip_spi_isr
- Return type: static irqreturn_t
- Signature: rockchip_spi_isr(int irq,void * dev_id)
- Line: 351

### rockchip_spi_max_transfer_size
- Return type: static size_t
- Signature: rockchip_spi_max_transfer_size(struct spi_device * spi)
- Line: 615

### rockchip_spi_pio_reader
- Return type: static void
- Signature: rockchip_spi_pio_reader(struct rockchip_spi * rs)
- Line: 317

### rockchip_spi_pio_writer
- Return type: static void
- Signature: rockchip_spi_pio_writer(struct rockchip_spi * rs)
- Line: 298

### rockchip_spi_prepare_dma
- Return type: static int
- Signature: rockchip_spi_prepare_dma(struct rockchip_spi * rs,struct spi_controller * ctlr,struct spi_transfer * xfer)
- Line: 450

### rockchip_spi_prepare_irq
- Return type: static int
- Signature: rockchip_spi_prepare_irq(struct rockchip_spi * rs,struct spi_controller * ctlr,struct spi_transfer * xfer)
- Line: 380

### rockchip_spi_probe
- Return type: static int
- Signature: rockchip_spi_probe(struct platform_device * pdev)
- Line: 755

### rockchip_spi_remove
- Return type: static void
- Signature: rockchip_spi_remove(struct platform_device * pdev)
- Line: 923

### rockchip_spi_resume
- Return type: static int
- Signature: rockchip_spi_resume(struct device * dev)
- Line: 962

### rockchip_spi_runtime_resume
- Return type: static int
- Signature: rockchip_spi_runtime_resume(struct device * dev)
- Line: 989

### rockchip_spi_runtime_suspend
- Return type: static int
- Signature: rockchip_spi_runtime_suspend(struct device * dev)
- Line: 978

### rockchip_spi_set_cs
- Return type: static void
- Signature: rockchip_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 236

### rockchip_spi_setup
- Return type: static int
- Signature: rockchip_spi_setup(struct spi_device * spi)
- Line: 727

### rockchip_spi_suspend
- Return type: static int
- Signature: rockchip_spi_suspend(struct device * dev)
- Line: 942

### rockchip_spi_target_abort
- Return type: static int
- Signature: rockchip_spi_target_abort(struct spi_controller * ctlr)
- Line: 620

### rockchip_spi_transfer_one
- Return type: static int
- Signature: rockchip_spi_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 671

### spi_enable_chip
- Return type: static void
- Signature: spi_enable_chip(struct rockchip_spi * rs,bool enable)
- Line: 198

### wait_for_tx_idle
- Return type: static void
- Signature: wait_for_tx_idle(struct rockchip_spi * rs,bool target_mode)
- Line: 203

## Structs (1)

### rockchip_spi
- Line: 166
- Members:
  - dev: device *
  - spiclk: clk *
  - apb_pclk: clk *
  - regs: void __iomem *
  - dma_addr_rx: dma_addr_t
  - dma_addr_tx: dma_addr_t
  - tx: const void *
  - rx: void *
  - tx_left: unsigned int
  - rx_left: unsigned int
  - state: atomic_t
  - fifo_len: u32
  - freq: u32
  - n_bytes: u8
  - rsd: u8
  - target_abort: bool
  - cs_inactive: bool
  - cs_high_supported: bool
  - xfer: spi_transfer *

## Variables (3)

- static **rockchip_spi_driver** : platform_driver (line 1030)
- static **rockchip_spi_dt_match** : const struct of_device_id[] (line 1013)
- static **rockchip_spi_pm** : const struct dev_pm_ops (line 1007)

## Macros (93)

- **BAUDR_SCKDV_MAX** (line 116)
- **BAUDR_SCKDV_MIN** (line 115)
- **CR0_BHT_16BIT** (line 89)
- **CR0_BHT_8BIT** (line 90)
- **CR0_BHT_OFFSET** (line 88)
- **CR0_CFS_OFFSET** (line 54)
- **CR0_CSM_HALF** (line 63)
- **CR0_CSM_KEEP** (line 61)
- **CR0_CSM_OFFSET** (line 60)
- **CR0_CSM_ONE** (line 65)
- **CR0_DFS_16BIT** (line 52)
- **CR0_DFS_4BIT** (line 50)
- **CR0_DFS_8BIT** (line 51)
- **CR0_DFS_OFFSET** (line 49)
- **CR0_EM_BIG** (line 82)
- **CR0_EM_LITTLE** (line 81)
- **CR0_EM_OFFSET** (line 80)
- **CR0_FBM_LSB** (line 86)
- **CR0_FBM_MSB** (line 85)
- **CR0_FBM_OFFSET** (line 84)
- **CR0_FRF_MICROWIRE** (line 98)
- **CR0_FRF_OFFSET** (line 95)
- **CR0_FRF_SPI** (line 96)
- **CR0_FRF_SSP** (line 97)
- **CR0_OPM_HOST** (line 106)
- **CR0_OPM_OFFSET** (line 105)
- **CR0_OPM_TARGET** (line 107)
- **CR0_RSD_MAX** (line 93)
- **CR0_RSD_OFFSET** (line 92)
- **CR0_SCPH_OFFSET** (line 56)
- **CR0_SCPOL_OFFSET** (line 58)
- **CR0_SOI_OFFSET** (line 109)
- **CR0_SSD_HALF** (line 73)
- **CR0_SSD_OFFSET** (line 68)
- **CR0_SSD_ONE** (line 78)
- **CR0_XFM_OFFSET** (line 100)
- **CR0_XFM_RO** (line 103)
- **CR0_XFM_TO** (line 102)
- **CR0_XFM_TR** (line 101)
- **DRIVER_NAME** (line 18)
- **ICR_ALL** (line 138)
- **ICR_MASK** (line 137)
- **ICR_RF_OVERFLOW** (line 140)
- **ICR_RF_UNDERFLOW** (line 139)
- **ICR_TF_OVERFLOW** (line 141)
- **INT_CS_INACTIVE** (line 134)
- **INT_MASK** (line 128)
- **INT_RF_FULL** (line 133)
- **INT_RF_OVERFLOW** (line 132)
- **INT_RF_UNDERFLOW** (line 131)
- **INT_TF_EMPTY** (line 129)
- **INT_TF_OVERFLOW** (line 130)
- **MAX_SCLK_OUT** (line 152)
- **RF_DMA_EN** (line 144)
- **ROCKCHIP_AUTOSUSPEND_TIMEOUT** (line 164)
- **ROCKCHIP_SPI_BAUDR** (line 30)
- **ROCKCHIP_SPI_CLR_BITS**(reg,bits) (line 20)
- **ROCKCHIP_SPI_CTRLR0** (line 26)
- **ROCKCHIP_SPI_CTRLR1** (line 27)
- **ROCKCHIP_SPI_DMACR** (line 41)
- **ROCKCHIP_SPI_DMARDLR** (line 43)
- **ROCKCHIP_SPI_DMATDLR** (line 42)
- **ROCKCHIP_SPI_ICR** (line 40)
- **ROCKCHIP_SPI_IMR** (line 37)
- **ROCKCHIP_SPI_IPR** (line 36)
- **ROCKCHIP_SPI_ISR** (line 38)
- **ROCKCHIP_SPI_MAX_NATIVE_CS_NUM** (line 160)
- **ROCKCHIP_SPI_MAX_TRANLEN** (line 158)
- **ROCKCHIP_SPI_RISR** (line 39)
- **ROCKCHIP_SPI_RXDR** (line 46)
- **ROCKCHIP_SPI_RXFLR** (line 34)
- **ROCKCHIP_SPI_RXFTLR** (line 32)
- **ROCKCHIP_SPI_SER** (line 29)
- **ROCKCHIP_SPI_SET_BITS**(reg,bits) (line 22)
- **ROCKCHIP_SPI_SR** (line 35)
- **ROCKCHIP_SPI_SSIENR** (line 28)
- **ROCKCHIP_SPI_TXDR** (line 45)
- **ROCKCHIP_SPI_TXFLR** (line 33)
- **ROCKCHIP_SPI_TXFTLR** (line 31)
- **ROCKCHIP_SPI_VER2_TYPE1** (line 161)
- **ROCKCHIP_SPI_VER2_TYPE2** (line 162)
- **ROCKCHIP_SPI_VERSION** (line 44)
- **RXDMA** (line 148)
- **SER_MASK** (line 112)
- **SR_BUSY** (line 120)
- **SR_MASK** (line 119)
- **SR_RF_EMPTY** (line 123)
- **SR_RF_FULL** (line 124)
- **SR_TARGET_TX_BUSY** (line 125)
- **SR_TF_EMPTY** (line 122)
- **SR_TF_FULL** (line 121)
- **TF_DMA_EN** (line 145)
- **TXDMA** (line 149)
