# drivers/mmc/host/toshsd.c

Subsystem: drivers/mmc

## Functions (19)

### __toshsd_set_ios
- Return type: static void
- Signature: __toshsd_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 78

### toshsd_cmd_irq
- Return type: static void
- Signature: toshsd_cmd_irq(struct toshsd_host * host)
- Line: 205

### toshsd_data_end_irq
- Return type: static void
- Signature: toshsd_data_end_irq(struct toshsd_host * host)
- Line: 265

### toshsd_finish_request
- Return type: static void
- Signature: toshsd_finish_request(struct toshsd_host * host)
- Line: 143

### toshsd_get_cd
- Return type: static int
- Signature: toshsd_get_cd(struct mmc_host * mmc)
- Line: 542

### toshsd_get_ro
- Return type: static int
- Signature: toshsd_get_ro(struct mmc_host * mmc)
- Line: 534

### toshsd_init
- Return type: static void
- Signature: toshsd_init(struct toshsd_host * host)
- Line: 35

### toshsd_irq
- Return type: static irqreturn_t
- Signature: toshsd_irq(int irq,void * dev_id)
- Line: 289

### toshsd_pm_resume
- Return type: static int
- Signature: toshsd_pm_resume(struct device * dev)
- Line: 585

### toshsd_pm_suspend
- Return type: static int
- Signature: toshsd_pm_suspend(struct device * dev)
- Line: 570

### toshsd_powerdown
- Return type: static void
- Signature: toshsd_powerdown(struct toshsd_host * host)
- Line: 557

### toshsd_probe
- Return type: static int
- Signature: toshsd_probe(struct pci_dev * pdev,const struct pci_device_id * ent)
- Line: 602

### toshsd_remove
- Return type: static void
- Signature: toshsd_remove(struct pci_dev * pdev)
- Line: 676

### toshsd_request
- Return type: static void
- Signature: toshsd_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 496

### toshsd_set_ios
- Return type: static void
- Signature: toshsd_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 524

### toshsd_set_led
- Return type: static void
- Signature: toshsd_set_led(struct toshsd_host * host,unsigned char state)
- Line: 138

### toshsd_start_cmd
- Return type: static void
- Signature: toshsd_start_cmd(struct toshsd_host * host,struct mmc_command * cmd)
- Line: 402

### toshsd_start_data
- Return type: static void
- Signature: toshsd_start_data(struct toshsd_host * host,struct mmc_data * data)
- Line: 474

### toshsd_thread_irq
- Return type: static irqreturn_t
- Signature: toshsd_thread_irq(int irq,void * dev_id)
- Line: 156

## Variables (3)

- static **pci_ids** : const struct pci_device_id[] (line 28)
- static **toshsd_driver** : pci_driver (line 691)
- static **toshsd_ops** : const struct mmc_host_ops (line 549)

## Macros (1)

- **DRIVER_NAME** (line 26)
