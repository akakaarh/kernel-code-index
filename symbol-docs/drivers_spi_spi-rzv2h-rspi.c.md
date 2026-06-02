# drivers/spi/spi-rzv2h-rspi.c

Subsystem: drivers/spi

## Functions (23)

### RZV2H_RSPI_TX
- Return type: static void
- Signature: RZV2H_RSPI_TX(writel,u32)
- Line: 135

### rzv2h_rspi_calc_bitrate
- Return type: static u32
- Signature: rzv2h_rspi_calc_bitrate(unsigned long tclk_rate,u8 spr,u8 brdv)
- Line: 409

### rzv2h_rspi_can_dma
- Return type: static bool
- Signature: rzv2h_rspi_can_dma(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 228

### rzv2h_rspi_clear_all_irqs
- Return type: static void
- Signature: rzv2h_rspi_clear_all_irqs(struct rzv2h_rspi_priv * rspi)
- Line: 167

### rzv2h_rspi_clear_fifos
- Return type: static void
- Signature: rzv2h_rspi_clear_fifos(const struct rzv2h_rspi_priv * rspi)
- Line: 162

### rzv2h_rspi_dma_complete
- Return type: static void
- Signature: rzv2h_rspi_dma_complete(void * arg)
- Line: 263

### rzv2h_rspi_dma_width
- Return type: static dma_slave_buswidth
- Signature: rzv2h_rspi_dma_width(struct rzv2h_rspi_priv * rspi)
- Line: 305

### rzv2h_rspi_find_rate_fixed
- Return type: static void
- Signature: rzv2h_rspi_find_rate_fixed(struct clk * clk,u32 hz,struct rzv2h_rspi_best_clock * best)
- Line: 513

### rzv2h_rspi_find_rate_variable
- Return type: static void
- Signature: rzv2h_rspi_find_rate_variable(struct clk * clk,u32 hz,struct rzv2h_rspi_best_clock * best)
- Line: 415

### rzv2h_rspi_prepare_message
- Return type: static int
- Signature: rzv2h_rspi_prepare_message(struct spi_controller * ctlr,struct spi_message * message)
- Line: 595

### rzv2h_rspi_probe
- Return type: static int
- Signature: rzv2h_rspi_probe(struct platform_device * pdev)
- Line: 693

### rzv2h_rspi_receive
- Return type: static int
- Signature: rzv2h_rspi_receive(struct rzv2h_rspi_priv * rspi,void * rxbuf,unsigned int index)
- Line: 205

### rzv2h_rspi_send
- Return type: static void
- Signature: rzv2h_rspi_send(struct rzv2h_rspi_priv * rspi,const void * txbuf,unsigned int index)
- Line: 190

### rzv2h_rspi_setup_clock
- Return type: static u32
- Signature: rzv2h_rspi_setup_clock(struct rzv2h_rspi_priv * rspi,u32 hz)
- Line: 569

### rzv2h_rspi_setup_dma_channel
- Return type: static dma_async_tx_descriptor *
- Signature: rzv2h_rspi_setup_dma_channel(struct rzv2h_rspi_priv * rspi,struct dma_chan * chan,struct sg_table * sg,enum dma_slave_buswidth width,enum dma_transfer_direction direction)
- Line: 272

### rzv2h_rspi_spe_disable
- Return type: static void
- Signature: rzv2h_rspi_spe_disable(const struct rzv2h_rspi_priv * rspi)
- Line: 152

### rzv2h_rspi_spe_enable
- Return type: static void
- Signature: rzv2h_rspi_spe_enable(const struct rzv2h_rspi_priv * rspi)
- Line: 157

### rzv2h_rspi_transfer_dma
- Return type: static int
- Signature: rzv2h_rspi_transfer_dma(struct rzv2h_rspi_priv * rspi,struct spi_device * spi,struct spi_transfer * transfer,unsigned int words_to_transfer)
- Line: 319

### rzv2h_rspi_transfer_one
- Return type: static int
- Signature: rzv2h_rspi_transfer_one(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 383

### rzv2h_rspi_transfer_pio
- Return type: static int
- Signature: rzv2h_rspi_transfer_pio(struct rzv2h_rspi_priv * rspi,struct spi_device * spi,struct spi_transfer * transfer,unsigned int words_to_transfer)
- Line: 242

### rzv2h_rspi_unprepare_message
- Return type: static int
- Signature: rzv2h_rspi_unprepare_message(struct spi_controller * ctlr,struct spi_message * message)
- Line: 683

### rzv2h_rspi_wait_for_interrupt
- Return type: static int
- Signature: rzv2h_rspi_wait_for_interrupt(struct rzv2h_rspi_priv * rspi,u32 wait_mask)
- Line: 183

### rzv2h_rx_irq_handler
- Return type: static irqreturn_t
- Signature: rzv2h_rx_irq_handler(int irq,void * data)
- Line: 173

## Structs (3)

### rzv2h_rspi_best_clock
- Line: 81
- Members:
  - clk: clk *
  - clk_rate: unsigned long
  - error: unsigned long
  - actual_hz: u32
  - brdv: u8
  - spr: u8
  - find_tclk_rate: void (*)(struct clk * clk,u32 hz,struct rzv2h_rspi_best_clock * best_clk)
  - find_pclk_rate: void (*)(struct clk * clk,u32 hz,struct rzv2h_rspi_best_clock * best_clk)
  - tclk_name: const char *
  - fifo_size: unsigned int
  - num_clks: unsigned int
  - controller: spi_controller *
  - info: const struct rzv2h_rspi_info *
  - pdev: platform_device *
  - base: void __iomem *
  - tclk: clk *
  - pclk: clk *
  - wait: wait_queue_head_t
  - bytes_per_word: unsigned int
  - irq_rx: int
  - last_speed_hz: u32
  - freq: u32
  - status: u16
  - spr: u8
  - brdv: u8
  - use_pclk: bool
  - dma_callbacked: bool

### rzv2h_rspi_info
- Line: 90
- Members:
  - clk: clk *
  - clk_rate: unsigned long
  - error: unsigned long
  - actual_hz: u32
  - brdv: u8
  - spr: u8
  - find_tclk_rate: void (*)(struct clk * clk,u32 hz,struct rzv2h_rspi_best_clock * best_clk)
  - find_pclk_rate: void (*)(struct clk * clk,u32 hz,struct rzv2h_rspi_best_clock * best_clk)
  - tclk_name: const char *
  - fifo_size: unsigned int
  - num_clks: unsigned int
  - controller: spi_controller *
  - info: const struct rzv2h_rspi_info *
  - pdev: platform_device *
  - base: void __iomem *
  - tclk: clk *
  - pclk: clk *
  - wait: wait_queue_head_t
  - bytes_per_word: unsigned int
  - irq_rx: int
  - last_speed_hz: u32
  - freq: u32
  - status: u16
  - spr: u8
  - brdv: u8
  - use_pclk: bool
  - dma_callbacked: bool

### rzv2h_rspi_priv
- Line: 100
- Members:
  - clk: clk *
  - clk_rate: unsigned long
  - error: unsigned long
  - actual_hz: u32
  - brdv: u8
  - spr: u8
  - find_tclk_rate: void (*)(struct clk * clk,u32 hz,struct rzv2h_rspi_best_clock * best_clk)
  - find_pclk_rate: void (*)(struct clk * clk,u32 hz,struct rzv2h_rspi_best_clock * best_clk)
  - tclk_name: const char *
  - fifo_size: unsigned int
  - num_clks: unsigned int
  - controller: spi_controller *
  - info: const struct rzv2h_rspi_info *
  - pdev: platform_device *
  - base: void __iomem *
  - tclk: clk *
  - pclk: clk *
  - wait: wait_queue_head_t
  - bytes_per_word: unsigned int
  - irq_rx: int
  - last_speed_hz: u32
  - freq: u32
  - status: u16
  - spr: u8
  - brdv: u8
  - use_pclk: bool
  - dma_callbacked: bool

## Variables (5)

- static **rzg3l_info** : const struct rzv2h_rspi_info (line 812)
- static **rzt2h_info** : const struct rzv2h_rspi_info (line 819)
- static **rzv2h_info** : const struct rzv2h_rspi_info (line 805)
- static **rzv2h_rspi_drv** : platform_driver (line 835)
- static **rzv2h_rspi_match** : const struct of_device_id[] (line 827)

## Macros (37)

- **RSPI_MAX_SPEED_HZ** (line 79)
- **RSPI_RESET_NUM** (line 77)
- **RSPI_SPBR** (line 32)
- **RSPI_SPBR_SPR_MAX** (line 53)
- **RSPI_SPBR_SPR_MIN** (line 52)
- **RSPI_SPCMD** (line 34)
- **RSPI_SPCMD_BRDV** (line 60)
- **RSPI_SPCMD_BRDV_MAX** (line 65)
- **RSPI_SPCMD_BRDV_MIN** (line 64)
- **RSPI_SPCMD_CPHA** (line 62)
- **RSPI_SPCMD_CPOL** (line 61)
- **RSPI_SPCMD_LSBF** (line 58)
- **RSPI_SPCMD_SPB** (line 57)
- **RSPI_SPCMD_SSLA** (line 56)
- **RSPI_SPCMD_SSLKP** (line 59)
- **RSPI_SPCR** (line 29)
- **RSPI_SPCR_BPEN** (line 41)
- **RSPI_SPCR_MSTR** (line 42)
- **RSPI_SPCR_SCKASE** (line 45)
- **RSPI_SPCR_SPE** (line 46)
- **RSPI_SPCR_SPRIE** (line 44)
- **RSPI_SPCR_SPTIE** (line 43)
- **RSPI_SPDCR2** (line 35)
- **RSPI_SPDCR2_RTRG** (line 69)
- **RSPI_SPDCR2_TTRG** (line 68)
- **RSPI_SPDR** (line 28)
- **RSPI_SPFCR** (line 38)
- **RSPI_SPPCR** (line 30)
- **RSPI_SPPCR_SPLP2** (line 49)
- **RSPI_SPSCR** (line 33)
- **RSPI_SPSR** (line 36)
- **RSPI_SPSRC** (line 37)
- **RSPI_SPSRC_CLEAR** (line 75)
- **RSPI_SPSR_SPRF** (line 72)
- **RSPI_SSLP** (line 31)
- **RZV2H_RSPI_RX**(func,type) (line 127)
- **RZV2H_RSPI_TX**(func,type) (line 119)
