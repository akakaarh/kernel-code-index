# drivers/mmc/host/wbsd.c

Subsystem: drivers/mmc

## Functions (58)

### wbsd_alloc_mmc
- Return type: static int
- Signature: wbsd_alloc_mmc(struct device * dev)
- Line: 1185

### wbsd_card_bh_work
- Return type: static void
- Signature: wbsd_card_bh_work(struct work_struct * t)
- Line: 990

### wbsd_chip_config
- Return type: static void
- Signature: wbsd_chip_config(struct wbsd_host * host)
- Line: 1526

### wbsd_chip_poweroff
- Return type: static void
- Signature: wbsd_chip_poweroff(struct wbsd_host * host)
- Line: 1610

### wbsd_chip_validate
- Return type: static int
- Signature: wbsd_chip_validate(struct wbsd_host * host)
- Line: 1570

### wbsd_crc_bh_work
- Return type: static void
- Signature: wbsd_crc_bh_work(struct work_struct * t)
- Line: 1070

### wbsd_dma_to_sg
- Return type: static void
- Signature: wbsd_dma_to_sg(struct wbsd_host * host,struct mmc_data * data)
- Line: 283

### wbsd_drv_exit
- Return type: static void __exit
- Signature: wbsd_drv_exit(void)
- Line: 1963

### wbsd_drv_init
- Return type: static int __init
- Signature: wbsd_drv_init(void)
- Line: 1924

### wbsd_empty_fifo
- Return type: static void
- Signature: wbsd_empty_fifo(struct wbsd_host * host)
- Line: 400

### wbsd_fifo_bh_work
- Return type: static void
- Signature: wbsd_fifo_bh_work(struct work_struct * t)
- Line: 1039

### wbsd_fill_fifo
- Return type: static void
- Signature: wbsd_fill_fifo(struct wbsd_host * host)
- Line: 465

### wbsd_finish_bh_work
- Return type: static void
- Signature: wbsd_finish_bh_work(struct work_struct * t)
- Line: 1118

### wbsd_finish_data
- Return type: static void
- Signature: wbsd_finish_data(struct wbsd_host * host,struct mmc_data * data)
- Line: 665

### wbsd_free_mmc
- Return type: static void
- Signature: wbsd_free_mmc(struct device * dev)
- Line: 1252

### wbsd_get_data
- Return type: static mmc_data *
- Signature: wbsd_get_data(struct wbsd_host * host)
- Line: 973

### wbsd_get_long_reply
- Return type: static void
- Signature: wbsd_get_long_reply(struct wbsd_host * host,struct mmc_command * cmd)
- Line: 315

### wbsd_get_ro
- Return type: static int
- Signature: wbsd_get_ro(struct mmc_host * mmc)
- Line: 910

### wbsd_get_short_reply
- Return type: static void
- Signature: wbsd_get_short_reply(struct wbsd_host * host,struct mmc_command * cmd)
- Line: 297

### wbsd_init
- Return type: static int
- Signature: wbsd_init(struct device * dev,int base,int irq,int dma,int pnp)
- Line: 1626

### wbsd_init_device
- Return type: static void
- Signature: wbsd_init_device(struct wbsd_host * host)
- Line: 131

### wbsd_init_sg
- Return type: static void
- Signature: wbsd_init_sg(struct wbsd_host * host,struct mmc_data * data)
- Line: 237

### wbsd_irq
- Return type: static irqreturn_t
- Signature: wbsd_irq(int irq,void * dev_id)
- Line: 1143

### wbsd_lock_config
- Return type: static void
- Signature: wbsd_lock_config(struct wbsd_host * host)
- Line: 92

### wbsd_map_sg
- Return type: static char *
- Signature: wbsd_map_sg(struct wbsd_host * host)
- Line: 268

### wbsd_next_sg
- Return type: static int
- Signature: wbsd_next_sg(struct wbsd_host * host)
- Line: 249

### wbsd_platform_resume
- Return type: static int
- Signature: wbsd_platform_resume(struct platform_device * dev)
- Line: 1814

### wbsd_platform_suspend
- Return type: static int
- Signature: wbsd_platform_suspend(struct platform_device * dev,pm_message_t state)
- Line: 1797

### wbsd_pnp_probe
- Return type: static int
- Signature: wbsd_pnp_probe(struct pnp_dev * pnpdev,const struct pnp_device_id * dev_id)
- Line: 1765

### wbsd_pnp_remove
- Return type: static void
- Signature: wbsd_pnp_remove(struct pnp_dev * dev)
- Line: 1784

### wbsd_pnp_resume
- Return type: static int
- Signature: wbsd_pnp_resume(struct pnp_dev * pnp_dev)
- Line: 1850

### wbsd_pnp_suspend
- Return type: static int
- Signature: wbsd_pnp_suspend(struct pnp_dev * pnp_dev,pm_message_t state)
- Line: 1839

### wbsd_prepare_data
- Return type: static void
- Signature: wbsd_prepare_data(struct wbsd_host * host,struct mmc_data * data)
- Line: 530

### wbsd_probe
- Return type: static int
- Signature: wbsd_probe(struct platform_device * dev)
- Line: 1747

### wbsd_read_config
- Return type: static u8
- Signature: wbsd_read_config(struct wbsd_host * host,u8 reg)
- Line: 107

### wbsd_read_index
- Return type: static u8
- Signature: wbsd_read_index(struct wbsd_host * host,u8 index)
- Line: 121

### wbsd_release_dma
- Return type: static void
- Signature: wbsd_release_dma(struct wbsd_host * host)
- Line: 1417

### wbsd_release_irq
- Return type: static void
- Signature: wbsd_release_irq(struct wbsd_host * host)
- Line: 1464

### wbsd_release_regions
- Return type: static void
- Signature: wbsd_release_regions(struct wbsd_host * host)
- Line: 1338

### wbsd_release_resources
- Return type: static void
- Signature: wbsd_release_resources(struct wbsd_host * host)
- Line: 1515

### wbsd_remove
- Return type: static void
- Signature: wbsd_remove(struct platform_device * dev)
- Line: 1753

### wbsd_request
- Return type: static void
- Signature: wbsd_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 743

### wbsd_request_dma
- Return type: static void
- Signature: wbsd_request_dma(struct wbsd_host * host,int dma)
- Line: 1355

### wbsd_request_end
- Return type: static void
- Signature: wbsd_request_end(struct wbsd_host * host,struct mmc_request * mrq)
- Line: 204

### wbsd_request_irq
- Return type: static int
- Signature: wbsd_request_irq(struct wbsd_host * host,int irq)
- Line: 1439

### wbsd_request_region
- Return type: static int
- Signature: wbsd_request_region(struct wbsd_host * host,int base)
- Line: 1325

### wbsd_request_resources
- Return type: static int
- Signature: wbsd_request_resources(struct wbsd_host * host,int base,int irq,int dma)
- Line: 1484

### wbsd_reset
- Return type: static void
- Signature: wbsd_reset(struct wbsd_host * host)
- Line: 190

### wbsd_reset_ignore
- Return type: static void
- Signature: wbsd_reset_ignore(struct timer_list * t)
- Line: 948

### wbsd_scan
- Return type: static int
- Signature: wbsd_scan(struct wbsd_host * host)
- Line: 1271

### wbsd_send_command
- Return type: static void
- Signature: wbsd_send_command(struct wbsd_host * host,struct mmc_command * cmd)
- Line: 340

### wbsd_set_ios
- Return type: static void
- Signature: wbsd_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 837

### wbsd_sg_to_dma
- Return type: static void
- Signature: wbsd_sg_to_dma(struct wbsd_host * host,struct mmc_data * data)
- Line: 273

### wbsd_shutdown
- Return type: static void
- Signature: wbsd_shutdown(struct device * dev,int pnp)
- Line: 1720

### wbsd_timeout_bh_work
- Return type: static void
- Signature: wbsd_timeout_bh_work(struct work_struct * t)
- Line: 1094

### wbsd_unlock_config
- Return type: static void
- Signature: wbsd_unlock_config(struct wbsd_host * host)
- Line: 84

### wbsd_write_config
- Return type: static void
- Signature: wbsd_write_config(struct wbsd_host * host,u8 reg,u8 value)
- Line: 99

### wbsd_write_index
- Return type: static void
- Signature: wbsd_write_index(struct wbsd_host * host,u8 index,u8 value)
- Line: 115

## Variables (13)

- static **config_ports** : const int[] (line 64)
- static **param_dma** : int (line 78)
- static **param_io** : unsigned int (line 76)
- static **param_irq** : unsigned int (line 77)
- static **param_nopnp** : const unsigned int (line 74)
- static **param_nopnp** : unsigned int (line 72)
- static **pnp_dev_table** : const struct pnp_device_id[] (line 54)
- static **unlock_codes** : const int[] (line 65)
- static **valid_ids** : const int[] (line 67)
- static **wbsd_device** : platform_device * (line 1893)
- static **wbsd_driver** : platform_driver (line 1895)
- static **wbsd_ops** : const struct mmc_host_ops (line 932)
- static **wbsd_pnp_driver** : pnp_driver (line 1908)

## Macros (7)

- **DBG**(x...) (line 43)
- **DBGF**(f,x...) (line 45)
- **DRIVER_NAME** (line 41)
- **wbsd_platform_resume** (line 1886)
- **wbsd_platform_suspend** (line 1885)
- **wbsd_pnp_resume** (line 1889)
- **wbsd_pnp_suspend** (line 1888)
