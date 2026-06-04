# drivers/mmc/host/pxamci.c

Subsystem: drivers/mmc

## Functions (21)

### pxamci_cmd_done
- Return type: static int
- Signature: pxamci_cmd_done(struct pxamci_host * host,unsigned int stat)
- Line: 274

### pxamci_data_done
- Return type: static int
- Signature: pxamci_data_done(struct pxamci_host * host,unsigned int stat)
- Line: 329

### pxamci_detect_irq
- Return type: static irqreturn_t
- Signature: pxamci_detect_irq(int irq,void * devid)
- Line: 561

### pxamci_disable_irq
- Return type: static void
- Signature: pxamci_disable_irq(struct pxamci_host * host,unsigned int mask)
- Line: 146

### pxamci_dma_irq
- Return type: static void
- Signature: pxamci_dma_irq(void * param)
- Line: 528

### pxamci_enable_irq
- Return type: static void
- Signature: pxamci_enable_irq(struct pxamci_host * host,unsigned int mask)
- Line: 136

### pxamci_enable_sdio_irq
- Return type: static void
- Signature: pxamci_enable_sdio_irq(struct mmc_host * host,int enable)
- Line: 510

### pxamci_finish_request
- Return type: static void
- Signature: pxamci_finish_request(struct pxamci_host * host,struct mmc_request * mrq)
- Line: 266

### pxamci_get_ro
- Return type: static int
- Signature: pxamci_get_ro(struct mmc_host * mmc)
- Line: 425

### pxamci_init_ocr
- Return type: static int
- Signature: pxamci_init_ocr(struct pxamci_host * host)
- Line: 76

### pxamci_irq
- Return type: static irqreturn_t
- Signature: pxamci_irq(int irq,void * devid)
- Line: 373

### pxamci_of_init
- Return type: static int
- Signature: pxamci_of_init(struct platform_device * pdev,struct mmc_host * mmc)
- Line: 577

### pxamci_of_init
- Return type: static int
- Signature: pxamci_of_init(struct platform_device * pdev,struct mmc_host * mmc)
- Line: 599

### pxamci_probe
- Return type: static int
- Signature: pxamci_probe(struct platform_device * pdev)
- Line: 606

### pxamci_remove
- Return type: static void
- Signature: pxamci_remove(struct platform_device * pdev)
- Line: 757

### pxamci_request
- Return type: static void
- Signature: pxamci_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 399

### pxamci_set_ios
- Return type: static void
- Signature: pxamci_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 440

### pxamci_set_power
- Return type: static int
- Signature: pxamci_set_power(struct pxamci_host * host,unsigned char power_mode,unsigned int vdd)
- Line: 95

### pxamci_setup_data
- Return type: static void
- Signature: pxamci_setup_data(struct pxamci_host * host,struct mmc_data * data)
- Line: 158

### pxamci_start_cmd
- Return type: static void
- Signature: pxamci_start_cmd(struct pxamci_host * host,struct mmc_command * cmd,unsigned int cmdat)
- Line: 232

### pxamci_stop_clock
- Return type: static void
- Signature: pxamci_stop_clock(struct pxamci_host * host)
- Line: 116

## Structs (1)

### pxamci_host
- Line: 49
- Members:
  - mmc: mmc_host *
  - lock: spinlock_t
  - res: resource *
  - base: void __iomem *
  - clk: clk *
  - clkrate: unsigned long
  - clkrt: unsigned int
  - cmdat: unsigned int
  - imask: unsigned int
  - power_mode: unsigned int
  - detect_delay_ms: unsigned long
  - use_ro_gpio: bool
  - power: gpio_desc *
  - pdata: pxamci_platform_data *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - dma_chan_rx: dma_chan *
  - dma_chan_tx: dma_chan *
  - dma_cookie: dma_cookie_t
  - dma_len: unsigned int
  - dma_dir: unsigned int

## Variables (3)

- static **pxa_mmc_dt_ids** : const struct of_device_id[] (line 570)
- static **pxamci_driver** : platform_driver (line 779)
- static **pxamci_ops** : const struct mmc_host_ops (line 520)

## Macros (5)

- **CLKRT_OFF** (line 44)
- **DRIVER_NAME** (line 41)
- **NR_SG** (line 43)
- **RSP_TYPE**(x) (line 240)
- **mmc_has_26MHz**() (line 46)
