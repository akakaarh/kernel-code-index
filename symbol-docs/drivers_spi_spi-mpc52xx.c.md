# drivers/spi/spi-mpc52xx.c

Subsystem: drivers/spi

## Functions (11)

### mpc52xx_spi_chipsel
- Return type: static void
- Signature: mpc52xx_spi_chipsel(struct mpc52xx_spi * ms,int value)
- Line: 100

### mpc52xx_spi_fsm_process
- Return type: static void
- Signature: mpc52xx_spi_fsm_process(int irq,struct mpc52xx_spi * ms)
- Line: 322

### mpc52xx_spi_fsmstate_idle
- Return type: static int
- Signature: mpc52xx_spi_fsmstate_idle(int irq,struct mpc52xx_spi * ms,u8 status,u8 data)
- Line: 149

### mpc52xx_spi_fsmstate_transfer
- Return type: static int
- Signature: mpc52xx_spi_fsmstate_transfer(int irq,struct mpc52xx_spi * ms,u8 status,u8 data)
- Line: 215

### mpc52xx_spi_fsmstate_wait
- Return type: static int
- Signature: mpc52xx_spi_fsmstate_wait(int irq,struct mpc52xx_spi * ms,u8 status,u8 data)
- Line: 281

### mpc52xx_spi_irq
- Return type: static irqreturn_t
- Signature: mpc52xx_spi_irq(int irq,void * _ms)
- Line: 342

### mpc52xx_spi_probe
- Return type: static int
- Signature: mpc52xx_spi_probe(struct platform_device * op)
- Line: 387

### mpc52xx_spi_remove
- Return type: static void
- Signature: mpc52xx_spi_remove(struct platform_device * op)
- Line: 517

### mpc52xx_spi_start_transfer
- Return type: static void
- Signature: mpc52xx_spi_start_transfer(struct mpc52xx_spi * ms)
- Line: 117

### mpc52xx_spi_transfer
- Return type: static int
- Signature: mpc52xx_spi_transfer(struct spi_device * spi,struct spi_message * m)
- Line: 368

### mpc52xx_spi_wq
- Return type: static void
- Signature: mpc52xx_spi_wq(struct work_struct * work)
- Line: 354

## Structs (1)

### mpc52xx_spi
- Line: 65
- Members:
  - host: spi_controller *
  - regs: void __iomem *
  - irq0: int
  - irq1: int
  - ipb_freq: unsigned int
  - msg_count: int
  - wcol_count: int
  - wcol_ticks: int
  - wcol_tx_timestamp: u32
  - modf_count: int
  - byte_count: int
  - queue: list_head
  - lock: spinlock_t
  - work: work_struct
  - message: spi_message *
  - transfer: spi_transfer *
  - state: int (*)(int irq,struct mpc52xx_spi * ms,u8 status,u8 data)
  - len: int
  - timestamp: int
  - rx_buf: u8 *
  - tx_buf: const u8 *
  - cs_change: int
  - gpio_cs_count: int
  - gpio_cs: gpio_desc **

## Variables (2)

- static **mpc52xx_spi_match** : const struct of_device_id[] (line 538)
- static **mpc52xx_spi_of_driver** : platform_driver (line 544)

## Macros (20)

- **FSM_CONTINUE** (line 62)
- **FSM_POLL** (line 60)
- **FSM_STOP** (line 57)
- **SPI_BRR** (line 45)
- **SPI_CTRL1** (line 35)
- **SPI_CTRL1_CPHA** (line 40)
- **SPI_CTRL1_CPOL** (line 39)
- **SPI_CTRL1_LSBFE** (line 42)
- **SPI_CTRL1_MSTR** (line 38)
- **SPI_CTRL1_SPE** (line 37)
- **SPI_CTRL1_SPIE** (line 36)
- **SPI_CTRL1_SSOE** (line 41)
- **SPI_CTRL2** (line 44)
- **SPI_DATA** (line 52)
- **SPI_DATADIR** (line 54)
- **SPI_PORTDATA** (line 53)
- **SPI_STATUS** (line 47)
- **SPI_STATUS_MODF** (line 50)
- **SPI_STATUS_SPIF** (line 48)
- **SPI_STATUS_WCOL** (line 49)
