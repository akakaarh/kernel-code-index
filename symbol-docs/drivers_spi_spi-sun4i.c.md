# drivers/spi/spi-sun4i.c

Subsystem: drivers/spi

## Functions (15)

### sun4i_spi_disable_interrupt
- Return type: static void
- Signature: sun4i_spi_disable_interrupt(struct sun4i_spi * sspi,u32 mask)
- Line: 117

### sun4i_spi_drain_fifo
- Return type: static void
- Signature: sun4i_spi_drain_fifo(struct sun4i_spi * sspi,int len)
- Line: 125

### sun4i_spi_enable_interrupt
- Return type: static void
- Signature: sun4i_spi_enable_interrupt(struct sun4i_spi * sspi,u32 mask)
- Line: 109

### sun4i_spi_fill_fifo
- Return type: static void
- Signature: sun4i_spi_fill_fifo(struct sun4i_spi * sspi,int len)
- Line: 145

### sun4i_spi_get_tx_fifo_count
- Return type: static u32
- Signature: sun4i_spi_get_tx_fifo_count(struct sun4i_spi * sspi)
- Line: 100

### sun4i_spi_handler
- Return type: static irqreturn_t
- Signature: sun4i_spi_handler(int irq,void * dev_id)
- Line: 353

### sun4i_spi_max_transfer_size
- Return type: static size_t
- Signature: sun4i_spi_max_transfer_size(struct spi_device * spi)
- Line: 199

### sun4i_spi_probe
- Return type: static int
- Signature: sun4i_spi_probe(struct platform_device * pdev)
- Line: 431

### sun4i_spi_read
- Return type: static u32
- Signature: sun4i_spi_read(struct sun4i_spi * sspi,u32 reg)
- Line: 90

### sun4i_spi_remove
- Return type: static void
- Signature: sun4i_spi_remove(struct platform_device * pdev)
- Line: 523

### sun4i_spi_runtime_resume
- Return type: static int
- Signature: sun4i_spi_runtime_resume(struct device * dev)
- Line: 391

### sun4i_spi_runtime_suspend
- Return type: static int
- Signature: sun4i_spi_runtime_suspend(struct device * dev)
- Line: 420

### sun4i_spi_set_cs
- Return type: static void
- Signature: sun4i_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 162

### sun4i_spi_transfer_one
- Return type: static int
- Signature: sun4i_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * tfr)
- Line: 204

### sun4i_spi_write
- Return type: static void
- Signature: sun4i_spi_write(struct sun4i_spi * sspi,u32 reg,u32 value)
- Line: 95

## Structs (1)

### sun4i_spi
- Line: 77
- Members:
  - host: spi_controller *
  - base_addr: void __iomem *
  - hclk: clk *
  - mclk: clk *
  - done: completion
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - len: int

## Variables (3)

- static **sun4i_spi_driver** : platform_driver (line 547)
- static **sun4i_spi_match** : const struct of_device_id[] (line 536)
- static **sun4i_spi_pm_ops** : const struct dev_pm_ops (line 542)

## Macros (42)

- **SUN4I_BURST_CNT**(cnt) (line 65)
- **SUN4I_BURST_CNT_REG** (line 64)
- **SUN4I_CLK_CTL_CDR1**(div) (line 59)
- **SUN4I_CLK_CTL_CDR1_MASK** (line 58)
- **SUN4I_CLK_CTL_CDR2**(div) (line 57)
- **SUN4I_CLK_CTL_CDR2_MASK** (line 56)
- **SUN4I_CLK_CTL_DRS** (line 60)
- **SUN4I_CLK_CTL_REG** (line 55)
- **SUN4I_CTL_CPHA** (line 30)
- **SUN4I_CTL_CPOL** (line 31)
- **SUN4I_CTL_CS**(cs) (line 38)
- **SUN4I_CTL_CS_ACTIVE_LOW** (line 32)
- **SUN4I_CTL_CS_LEVEL** (line 41)
- **SUN4I_CTL_CS_MANUAL** (line 40)
- **SUN4I_CTL_CS_MASK** (line 37)
- **SUN4I_CTL_DHB** (line 39)
- **SUN4I_CTL_ENABLE** (line 28)
- **SUN4I_CTL_LMTF** (line 33)
- **SUN4I_CTL_MASTER** (line 29)
- **SUN4I_CTL_REG** (line 27)
- **SUN4I_CTL_RF_RST** (line 35)
- **SUN4I_CTL_TF_RST** (line 34)
- **SUN4I_CTL_TP** (line 42)
- **SUN4I_CTL_XCH** (line 36)
- **SUN4I_DMA_CTL_REG** (line 51)
- **SUN4I_FIFO_DEPTH** (line 21)
- **SUN4I_FIFO_STA_REG** (line 71)
- **SUN4I_FIFO_STA_RF_CNT_BITS** (line 73)
- **SUN4I_FIFO_STA_RF_CNT_MASK** (line 72)
- **SUN4I_FIFO_STA_TF_CNT_BITS** (line 75)
- **SUN4I_FIFO_STA_TF_CNT_MASK** (line 74)
- **SUN4I_INT_CTL_REG** (line 44)
- **SUN4I_INT_CTL_RF_F34** (line 45)
- **SUN4I_INT_CTL_TC** (line 47)
- **SUN4I_INT_CTL_TF_E34** (line 46)
- **SUN4I_INT_STA_REG** (line 49)
- **SUN4I_MAX_XFER_SIZE** (line 62)
- **SUN4I_RXDATA_REG** (line 23)
- **SUN4I_TXDATA_REG** (line 25)
- **SUN4I_WAIT_REG** (line 53)
- **SUN4I_XMIT_CNT**(cnt) (line 68)
- **SUN4I_XMIT_CNT_REG** (line 67)
