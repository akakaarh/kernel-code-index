# drivers/spi/spi-lantiq-ssc.c

Subsystem: drivers/spi

## Functions (36)

### hw_enter_active_mode
- Return type: static void
- Signature: hw_enter_active_mode(const struct lantiq_ssc_spi * spi)
- Line: 262

### hw_enter_config_mode
- Return type: static void
- Signature: hw_enter_config_mode(const struct lantiq_ssc_spi * spi)
- Line: 257

### hw_setup_bits_per_word
- Return type: static void
- Signature: hw_setup_bits_per_word(const struct lantiq_ssc_spi * spi,unsigned int bits_per_word)
- Line: 296

### hw_setup_clock_mode
- Return type: static void
- Signature: hw_setup_clock_mode(const struct lantiq_ssc_spi * spi,unsigned int mode)
- Line: 307

### hw_setup_speed_hz
- Return type: static void
- Signature: hw_setup_speed_hz(const struct lantiq_ssc_spi * spi,unsigned int max_speed_hz)
- Line: 267

### hw_setup_transfer
- Return type: static void
- Signature: hw_setup_transfer(struct lantiq_ssc_spi * spi,struct spi_device * spidev,struct spi_transfer * t)
- Line: 431

### intel_lgm_cfg_irq
- Return type: static int
- Signature: intel_lgm_cfg_irq(struct platform_device * pdev,struct lantiq_ssc_spi * spi)
- Line: 822

### intel_lgm_ssc_isr
- Return type: static irqreturn_t
- Signature: intel_lgm_ssc_isr(int irq,void * data)
- Line: 704

### lantiq_cfg_irq
- Return type: static int
- Signature: lantiq_cfg_irq(struct platform_device * pdev,struct lantiq_ssc_spi * spi)
- Line: 833

### lantiq_ssc_bussy_work
- Return type: static void
- Signature: lantiq_ssc_bussy_work(struct work_struct * work)
- Line: 759

### lantiq_ssc_err_interrupt
- Return type: static irqreturn_t
- Signature: lantiq_ssc_err_interrupt(int irq,void * data)
- Line: 665

### lantiq_ssc_handle_err
- Return type: static void
- Signature: lantiq_ssc_handle_err(struct spi_controller * host,struct spi_message * message)
- Line: 787

### lantiq_ssc_hw_init
- Return type: static void
- Signature: lantiq_ssc_hw_init(const struct lantiq_ssc_spi * spi)
- Line: 345

### lantiq_ssc_maskl
- Return type: static void
- Signature: lantiq_ssc_maskl(const struct lantiq_ssc_spi * spi,u32 clr,u32 set,u32 reg)
- Line: 200

### lantiq_ssc_prepare_message
- Return type: static int
- Signature: lantiq_ssc_prepare_message(struct spi_controller * host,struct spi_message * message)
- Line: 419

### lantiq_ssc_probe
- Return type: static int
- Signature: lantiq_ssc_probe(struct platform_device * pdev)
- Line: 904

### lantiq_ssc_readl
- Return type: static u32
- Signature: lantiq_ssc_readl(const struct lantiq_ssc_spi * spi,u32 reg)
- Line: 189

### lantiq_ssc_remove
- Return type: static void
- Signature: lantiq_ssc_remove(struct platform_device * pdev)
- Line: 1015

### lantiq_ssc_set_cs
- Return type: static void
- Signature: lantiq_ssc_set_cs(struct spi_device * spidev,bool enable)
- Line: 797

### lantiq_ssc_setup
- Return type: static int
- Signature: lantiq_ssc_setup(struct spi_device * spidev)
- Line: 388

### lantiq_ssc_transfer_one
- Return type: static int
- Signature: lantiq_ssc_transfer_one(struct spi_controller * host,struct spi_device * spidev,struct spi_transfer * t)
- Line: 811

### lantiq_ssc_unprepare_message
- Return type: static int
- Signature: lantiq_ssc_unprepare_message(struct spi_controller * host,struct spi_message * message)
- Line: 464

### lantiq_ssc_writel
- Return type: static void
- Signature: lantiq_ssc_writel(const struct lantiq_ssc_spi * spi,u32 val,u32 reg)
- Line: 194

### lantiq_ssc_xmit_interrupt
- Return type: static irqreturn_t
- Signature: lantiq_ssc_xmit_interrupt(int irq,void * data)
- Line: 624

### rx_fifo_flush
- Return type: static void
- Signature: rx_fifo_flush(const struct lantiq_ssc_spi * spi)
- Line: 247

### rx_fifo_level
- Return type: static unsigned int
- Signature: rx_fifo_level(const struct lantiq_ssc_spi * spi)
- Line: 218

### rx_fifo_read_full_duplex
- Return type: static void
- Signature: rx_fifo_read_full_duplex(struct lantiq_ssc_spi * spi)
- Line: 519

### rx_fifo_read_half_duplex
- Return type: static void
- Signature: rx_fifo_read_half_duplex(struct lantiq_ssc_spi * spi)
- Line: 565

### rx_fifo_reset
- Return type: static void
- Signature: rx_fifo_reset(const struct lantiq_ssc_spi * spi)
- Line: 231

### rx_request
- Return type: static void
- Signature: rx_request(struct lantiq_ssc_spi * spi)
- Line: 607

### transfer_start
- Return type: static int
- Signature: transfer_start(struct lantiq_ssc_spi * spi,struct spi_device * spidev,struct spi_transfer * t)
- Line: 722

### tx_fifo_flush
- Return type: static void
- Signature: tx_fifo_flush(const struct lantiq_ssc_spi * spi)
- Line: 252

### tx_fifo_free
- Return type: static unsigned int
- Signature: tx_fifo_free(const struct lantiq_ssc_spi * spi)
- Line: 226

### tx_fifo_level
- Return type: static unsigned int
- Signature: tx_fifo_level(const struct lantiq_ssc_spi * spi)
- Line: 210

### tx_fifo_reset
- Return type: static void
- Signature: tx_fifo_reset(const struct lantiq_ssc_spi * spi)
- Line: 239

### tx_fifo_write
- Return type: static void
- Signature: tx_fifo_write(struct lantiq_ssc_spi * spi)
- Line: 478

## Structs (2)

### lantiq_ssc_hwcfg
- Line: 155
- Members:
  - cfg_irq: int (*)(struct platform_device * pdev,struct lantiq_ssc_spi * spi)
  - irnen_r: unsigned int
  - irnen_t: unsigned int
  - irncr: unsigned int
  - irnicr: unsigned int
  - irq_ack: bool
  - fifo_size_mask: u32
  - host: spi_controller *
  - dev: device *
  - regbase: void __iomem *
  - spi_clk: clk *
  - fpi_clk: clk *
  - hwcfg: const struct lantiq_ssc_hwcfg *
  - lock: spinlock_t
  - wq: workqueue_struct *
  - work: work_struct
  - tx: const u8 *
  - rx: u8 *
  - tx_todo: unsigned int
  - rx_todo: unsigned int
  - bits_per_word: unsigned int
  - speed_hz: unsigned int
  - tx_fifo_size: unsigned int
  - rx_fifo_size: unsigned int
  - base_cs: unsigned int
  - fdx_tx_level: unsigned int

### lantiq_ssc_spi
- Line: 165
- Members:
  - cfg_irq: int (*)(struct platform_device * pdev,struct lantiq_ssc_spi * spi)
  - irnen_r: unsigned int
  - irnen_t: unsigned int
  - irncr: unsigned int
  - irnicr: unsigned int
  - irq_ack: bool
  - fifo_size_mask: u32
  - host: spi_controller *
  - dev: device *
  - regbase: void __iomem *
  - spi_clk: clk *
  - fpi_clk: clk *
  - hwcfg: const struct lantiq_ssc_hwcfg *
  - lock: spinlock_t
  - wq: workqueue_struct *
  - work: work_struct
  - tx: const u8 *
  - rx: u8 *
  - tx_todo: unsigned int
  - rx_todo: unsigned int
  - bits_per_word: unsigned int
  - speed_hz: unsigned int
  - tx_fifo_size: unsigned int
  - rx_fifo_size: unsigned int
  - base_cs: unsigned int
  - fdx_tx_level: unsigned int

## Variables (5)

- static **intel_ssc_lgm** : const struct lantiq_ssc_hwcfg (line 885)
- static **lantiq_ssc_driver** : platform_driver (line 1035)
- static **lantiq_ssc_match** : const struct of_device_id[] (line 895)
- static **lantiq_ssc_xrx** : const struct lantiq_ssc_hwcfg (line 875)
- static **lantiq_ssc_xway** : const struct lantiq_ssc_hwcfg (line 865)

## Macros (106)

- **LTQ_SPI_BRSTAT** (line 43)
- **LTQ_SPI_BRT** (line 42)
- **LTQ_SPI_CLC** (line 31)
- **LTQ_SPI_CLC_DISR** (line 59)
- **LTQ_SPI_CLC_DISS** (line 58)
- **LTQ_SPI_CLC_RMC_M** (line 57)
- **LTQ_SPI_CLC_RMC_S** (line 56)
- **LTQ_SPI_CLC_SMC_M** (line 55)
- **LTQ_SPI_CLC_SMC_S** (line 54)
- **LTQ_SPI_CON** (line 34)
- **LTQ_SPI_CON_AEN** (line 76)
- **LTQ_SPI_CON_BM_M** (line 70)
- **LTQ_SPI_CON_BM_S** (line 69)
- **LTQ_SPI_CON_EM** (line 71)
- **LTQ_SPI_CON_ENBV** (line 73)
- **LTQ_SPI_CON_HB** (line 82)
- **LTQ_SPI_CON_IDLE** (line 72)
- **LTQ_SPI_CON_LB** (line 79)
- **LTQ_SPI_CON_PH** (line 81)
- **LTQ_SPI_CON_PO** (line 80)
- **LTQ_SPI_CON_REN** (line 77)
- **LTQ_SPI_CON_RUEN** (line 74)
- **LTQ_SPI_CON_RXOFF** (line 83)
- **LTQ_SPI_CON_TEN** (line 78)
- **LTQ_SPI_CON_TUEN** (line 75)
- **LTQ_SPI_CON_TXOFF** (line 84)
- **LTQ_SPI_DMACON** (line 51)
- **LTQ_SPI_ERR_IRQ_NAME** (line 28)
- **LTQ_SPI_FGPO_CLROUTN_S** (line 139)
- **LTQ_SPI_FGPO_SETOUTN_S** (line 138)
- **LTQ_SPI_FPGO** (line 48)
- **LTQ_SPI_FRM_IRQ_NAME** (line 29)
- **LTQ_SPI_FSTAT** (line 41)
- **LTQ_SPI_FSTAT_RXFFL_S** (line 132)
- **LTQ_SPI_FSTAT_TXFFL_S** (line 133)
- **LTQ_SPI_GPOCON** (line 46)
- **LTQ_SPI_GPOCON_INVOUTN_S** (line 136)
- **LTQ_SPI_GPOCON_ISCSBN_S** (line 135)
- **LTQ_SPI_GPOSTAT** (line 47)
- **LTQ_SPI_ID** (line 33)
- **LTQ_SPI_ID_CFG_M** (line 66)
- **LTQ_SPI_ID_CFG_S** (line 65)
- **LTQ_SPI_ID_MOD_M** (line 64)
- **LTQ_SPI_ID_MOD_S** (line 63)
- **LTQ_SPI_ID_REV_M** (line 67)
- **LTQ_SPI_ID_RXFS_S** (line 62)
- **LTQ_SPI_ID_TXFS_S** (line 61)
- **LTQ_SPI_IRNEN** (line 52)
- **LTQ_SPI_IRNEN_ALL** (line 151)
- **LTQ_SPI_IRNEN_E** (line 146)
- **LTQ_SPI_IRNEN_F** (line 145)
- **LTQ_SPI_IRNEN_R_XRX** (line 149)
- **LTQ_SPI_IRNEN_R_XWAY** (line 148)
- **LTQ_SPI_IRNEN_TFI** (line 144)
- **LTQ_SPI_IRNEN_T_XRX** (line 150)
- **LTQ_SPI_IRNEN_T_XWAY** (line 147)
- **LTQ_SPI_PISEL** (line 32)
- **LTQ_SPI_RB** (line 38)
- **LTQ_SPI_RXCNT** (line 50)
- **LTQ_SPI_RXCNT_TODO_M** (line 142)
- **LTQ_SPI_RXFCON** (line 39)
- **LTQ_SPI_RXFCON_RXFEN** (line 126)
- **LTQ_SPI_RXFCON_RXFITL_S** (line 124)
- **LTQ_SPI_RXFCON_RXFLU** (line 125)
- **LTQ_SPI_RXREQ** (line 49)
- **LTQ_SPI_RXREQ_RXCNT_M** (line 141)
- **LTQ_SPI_RX_IRQ_NAME** (line 26)
- **LTQ_SPI_SFCON** (line 44)
- **LTQ_SPI_SFSTAT** (line 45)
- **LTQ_SPI_STAT** (line 35)
- **LTQ_SPI_STAT_AE** (line 91)
- **LTQ_SPI_STAT_BSY** (line 88)
- **LTQ_SPI_STAT_EN** (line 96)
- **LTQ_SPI_STAT_ERRORS** (line 97)
- **LTQ_SPI_STAT_ME** (line 94)
- **LTQ_SPI_STAT_MS** (line 95)
- **LTQ_SPI_STAT_RE** (line 92)
- **LTQ_SPI_STAT_RUE** (line 89)
- **LTQ_SPI_STAT_RXBV_M** (line 87)
- **LTQ_SPI_STAT_RXBV_S** (line 86)
- **LTQ_SPI_STAT_TE** (line 93)
- **LTQ_SPI_STAT_TUE** (line 90)
- **LTQ_SPI_TB** (line 37)
- **LTQ_SPI_TXFCON** (line 40)
- **LTQ_SPI_TXFCON_TXFEN** (line 130)
- **LTQ_SPI_TXFCON_TXFITL_S** (line 128)
- **LTQ_SPI_TXFCON_TXFLU** (line 129)
- **LTQ_SPI_TX_IRQ_NAME** (line 27)
- **LTQ_SPI_WHBSTATE** (line 36)
- **LTQ_SPI_WHBSTATE_CLRAE** (line 106)
- **LTQ_SPI_WHBSTATE_CLREN** (line 116)
- **LTQ_SPI_WHBSTATE_CLRME** (line 110)
- **LTQ_SPI_WHBSTATE_CLRMS** (line 114)
- **LTQ_SPI_WHBSTATE_CLRRE** (line 107)
- **LTQ_SPI_WHBSTATE_CLRRUE** (line 112)
- **LTQ_SPI_WHBSTATE_CLRTE** (line 108)
- **LTQ_SPI_WHBSTATE_CLRTUE** (line 105)
- **LTQ_SPI_WHBSTATE_CLR_ERRORS** (line 117)
- **LTQ_SPI_WHBSTATE_SETAE** (line 102)
- **LTQ_SPI_WHBSTATE_SETEN** (line 115)
- **LTQ_SPI_WHBSTATE_SETME** (line 109)
- **LTQ_SPI_WHBSTATE_SETMS** (line 113)
- **LTQ_SPI_WHBSTATE_SETRE** (line 103)
- **LTQ_SPI_WHBSTATE_SETRUE** (line 111)
- **LTQ_SPI_WHBSTATE_SETTE** (line 104)
- **LTQ_SPI_WHBSTATE_SETTUE** (line 101)
