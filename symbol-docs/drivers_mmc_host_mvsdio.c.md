# drivers/mmc/host/mvsdio.c

Subsystem: drivers/mmc

## Functions (13)

### mv_conf_mbus_windows
- Return type: static void
- Signature: mv_conf_mbus_windows(struct mvsd_host * host,const struct mbus_dram_target_info * dram)
- Line: 672

### mvsd_enable_sdio_irq
- Return type: static void
- Signature: mvsd_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 551

### mvsd_finish_cmd
- Return type: static u32
- Signature: mvsd_finish_cmd(struct mvsd_host * host,struct mmc_command * cmd,u32 err_status)
- Line: 241

### mvsd_finish_data
- Return type: static u32
- Signature: mvsd_finish_data(struct mvsd_host * host,struct mmc_data * data,u32 err_status)
- Line: 286

### mvsd_irq
- Return type: static irqreturn_t
- Signature: mvsd_irq(int irq,void * dev)
- Line: 344

### mvsd_power_down
- Return type: static void
- Signature: mvsd_power_down(struct mvsd_host * host)
- Line: 584

### mvsd_power_up
- Return type: static void
- Signature: mvsd_power_up(struct mvsd_host * host)
- Line: 570

### mvsd_probe
- Return type: static int
- Signature: mvsd_probe(struct platform_device * pdev)
- Line: 693

### mvsd_remove
- Return type: static void
- Signature: mvsd_remove(struct platform_device * pdev)
- Line: 790

### mvsd_request
- Return type: static void
- Signature: mvsd_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 136

### mvsd_set_ios
- Return type: static void
- Signature: mvsd_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 598

### mvsd_setup_data
- Return type: static int
- Signature: mvsd_setup_data(struct mvsd_host * host,struct mmc_data * data)
- Line: 56

### mvsd_timeout_timer
- Return type: static void
- Signature: mvsd_timeout_timer(struct timer_list * t)
- Line: 510

## Structs (1)

### mvsd_host
- Line: 34
- Members:
  - base: void __iomem *
  - mrq: mmc_request *
  - lock: spinlock_t
  - xfer_mode: unsigned int
  - intr_en: unsigned int
  - ctrl: unsigned int
  - pio_size: unsigned int
  - pio_ptr: void *
  - sg_frags: unsigned int
  - ns_per_clk: unsigned int
  - clock: unsigned int
  - base_clock: unsigned int
  - timer: timer_list
  - mmc: mmc_host *
  - dev: device *
  - clk: clk *

## Variables (5)

- static **maxfreq** : int (line 31)
- static **mvsd_driver** : platform_driver (line 810)
- static **mvsd_ops** : const struct mmc_host_ops (line 664)
- static **mvsdio_dt_ids** : const struct of_device_id[] (line 804)
- static **nodma** : int (line 32)

## Macros (3)

- **DRIVER_NAME** (line 29)
- **mvsd_read**(offs) (line 54)
- **mvsd_write**(offs,val) (line 53)
