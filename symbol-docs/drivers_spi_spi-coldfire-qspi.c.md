# drivers/spi/spi-coldfire-qspi.c

Subsystem: drivers/spi

## Functions (26)

### mcfqspi_cs_deselect
- Return type: static void
- Signature: mcfqspi_cs_deselect(struct mcfqspi * mcfqspi,u8 chip_select,bool cs_high)
- Line: 114

### mcfqspi_cs_select
- Return type: static void
- Signature: mcfqspi_cs_select(struct mcfqspi * mcfqspi,u8 chip_select,bool cs_high)
- Line: 108

### mcfqspi_cs_setup
- Return type: static int
- Signature: mcfqspi_cs_setup(struct mcfqspi * mcfqspi)
- Line: 120

### mcfqspi_cs_teardown
- Return type: static void
- Signature: mcfqspi_cs_teardown(struct mcfqspi * mcfqspi)
- Line: 126

### mcfqspi_irq_handler
- Return type: static irqreturn_t
- Signature: mcfqspi_irq_handler(int this_irq,void * dev_id)
- Line: 142

### mcfqspi_probe
- Return type: static int
- Signature: mcfqspi_probe(struct platform_device * pdev)
- Line: 338

### mcfqspi_qdlyr_spe
- Return type: static bool
- Signature: mcfqspi_qdlyr_spe(struct mcfqspi * mcfqspi)
- Line: 137

### mcfqspi_qmr_baud
- Return type: static u8
- Signature: mcfqspi_qmr_baud(u32 speed_hz)
- Line: 132

### mcfqspi_rd_qdlyr
- Return type: static u16
- Signature: mcfqspi_rd_qdlyr(struct mcfqspi * mcfqspi)
- Line: 78

### mcfqspi_rd_qdr
- Return type: static u16
- Signature: mcfqspi_rd_qdr(struct mcfqspi * mcfqspi)
- Line: 103

### mcfqspi_remove
- Return type: static void
- Signature: mcfqspi_remove(struct platform_device * pdev)
- Line: 434

### mcfqspi_resume
- Return type: static int
- Signature: mcfqspi_resume(struct device * dev)
- Line: 468

### mcfqspi_runtime_resume
- Return type: static int
- Signature: mcfqspi_runtime_resume(struct device * dev)
- Line: 490

### mcfqspi_runtime_suspend
- Return type: static int
- Signature: mcfqspi_runtime_suspend(struct device * dev)
- Line: 480

### mcfqspi_set_cs
- Return type: static void
- Signature: mcfqspi_set_cs(struct spi_device * spi,bool enable)
- Line: 287

### mcfqspi_setup
- Return type: static int
- Signature: mcfqspi_setup(struct spi_device * spi)
- Line: 324

### mcfqspi_suspend
- Return type: static int
- Signature: mcfqspi_suspend(struct device * dev)
- Line: 453

### mcfqspi_transfer_msg16
- Return type: static void
- Signature: mcfqspi_transfer_msg16(struct mcfqspi * mcfqspi,unsigned count,const u16 * txbuf,u16 * rxbuf)
- Line: 220

### mcfqspi_transfer_msg8
- Return type: static void
- Signature: mcfqspi_transfer_msg8(struct mcfqspi * mcfqspi,unsigned count,const u8 * txbuf,u8 * rxbuf)
- Line: 153

### mcfqspi_transfer_one
- Return type: static int
- Signature: mcfqspi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 298

### mcfqspi_wr_qar
- Return type: static void
- Signature: mcfqspi_wr_qar(struct mcfqspi * mcfqspi,u16 val)
- Line: 93

### mcfqspi_wr_qdlyr
- Return type: static void
- Signature: mcfqspi_wr_qdlyr(struct mcfqspi * mcfqspi,u16 val)
- Line: 73

### mcfqspi_wr_qdr
- Return type: static void
- Signature: mcfqspi_wr_qdr(struct mcfqspi * mcfqspi,u16 val)
- Line: 98

### mcfqspi_wr_qir
- Return type: static void
- Signature: mcfqspi_wr_qir(struct mcfqspi * mcfqspi,u16 val)
- Line: 88

### mcfqspi_wr_qmr
- Return type: static void
- Signature: mcfqspi_wr_qmr(struct mcfqspi * mcfqspi,u16 val)
- Line: 68

### mcfqspi_wr_qwr
- Return type: static void
- Signature: mcfqspi_wr_qwr(struct mcfqspi * mcfqspi,u16 val)
- Line: 83

## Structs (1)

### mcfqspi
- Line: 59
- Members:
  - iobase: void __iomem *
  - irq: int
  - clk: clk *
  - cs_control: mcfqspi_cs_control *
  - waitq: wait_queue_head_t

## Variables (2)

- static **mcfqspi_driver** : platform_driver (line 507)
- static **mcfqspi_pm** : const struct dev_pm_ops (line 501)

## Macros (31)

- **DRIVER_NAME** (line 25)
- **MCFQSPI_BUSCLK** (line 27)
- **MCFQSPI_QAR** (line 49)
- **MCFQSPI_QAR_CMDBUF** (line 52)
- **MCFQSPI_QAR_RXBUF** (line 51)
- **MCFQSPI_QAR_TXBUF** (line 50)
- **MCFQSPI_QCR** (line 54)
- **MCFQSPI_QCR_BITSE** (line 56)
- **MCFQSPI_QCR_CONT** (line 55)
- **MCFQSPI_QCR_DT** (line 57)
- **MCFQSPI_QDLYR** (line 33)
- **MCFQSPI_QDLYR_SPE** (line 34)
- **MCFQSPI_QDR** (line 53)
- **MCFQSPI_QIR** (line 39)
- **MCFQSPI_QIR_ABRT** (line 47)
- **MCFQSPI_QIR_ABRTB** (line 41)
- **MCFQSPI_QIR_ABRTE** (line 44)
- **MCFQSPI_QIR_ABRTL** (line 42)
- **MCFQSPI_QIR_SPIF** (line 48)
- **MCFQSPI_QIR_SPIFE** (line 45)
- **MCFQSPI_QIR_WCEF** (line 46)
- **MCFQSPI_QIR_WCEFB** (line 40)
- **MCFQSPI_QIR_WCEFE** (line 43)
- **MCFQSPI_QMR** (line 29)
- **MCFQSPI_QMR_CPHA** (line 32)
- **MCFQSPI_QMR_CPOL** (line 31)
- **MCFQSPI_QMR_MSTR** (line 30)
- **MCFQSPI_QWR** (line 35)
- **MCFQSPI_QWR_CSIV** (line 38)
- **MCFQSPI_QWR_HALT** (line 36)
- **MCFQSPI_QWR_WREN** (line 37)
