# drivers/mmc/core/sd.c

Subsystem: drivers/mmc

## Functions (45)

### _mmc_sd_resume
- Return type: static int
- Signature: _mmc_sd_resume(struct mmc_host * host)
- Line: 1771

### _mmc_sd_suspend
- Return type: static int
- Signature: _mmc_sd_suspend(struct mmc_host * host)
- Line: 1713

### mmc_attach_sd
- Return type: int
- Signature: mmc_attach_sd(struct mmc_host * host)
- Line: 1854

### mmc_decode_cid
- Return type: void
- Signature: mmc_decode_cid(struct mmc_card * card)
- Line: 71

### mmc_decode_csd
- Return type: static int
- Signature: mmc_decode_csd(struct mmc_card * card,bool is_sduc)
- Line: 107

### mmc_decode_scr
- Return type: int
- Signature: mmc_decode_scr(struct mmc_card * card)
- Line: 207

### mmc_dsr_show
- Return type: static ssize_t
- Signature: mmc_dsr_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 732

### mmc_read_ssr
- Return type: static int
- Signature: mmc_read_ssr(struct mmc_card * card)
- Line: 257

### mmc_read_switch
- Return type: static int
- Signature: mmc_read_switch(struct mmc_card * card)
- Line: 322

### mmc_sd_alive
- Return type: static int
- Signature: mmc_sd_alive(struct mmc_host * host)
- Line: 1615

### mmc_sd_card_using_v18
- Return type: static bool
- Signature: mmc_sd_card_using_v18(struct mmc_card * card)
- Line: 1022

### mmc_sd_detect
- Return type: static void
- Signature: mmc_sd_detect(struct mmc_host * host)
- Line: 1623

### mmc_sd_get_cid
- Return type: int
- Signature: mmc_sd_get_cid(struct mmc_host * host,u32 ocr,u32 * cid,u32 * rocr)
- Line: 828

### mmc_sd_get_csd
- Return type: int
- Signature: mmc_sd_get_csd(struct mmc_card * card,bool is_sduc)
- Line: 905

### mmc_sd_get_max_clock
- Return type: unsigned
- Signature: mmc_sd_get_max_clock(struct mmc_card * card)
- Line: 1008

### mmc_sd_get_ro
- Return type: int
- Signature: mmc_sd_get_ro(struct mmc_host * host)
- Line: 923

### mmc_sd_hw_reset
- Return type: static int
- Signature: mmc_sd_hw_reset(struct mmc_host * host)
- Line: 1831

### mmc_sd_init_card
- Return type: static int
- Signature: mmc_sd_init_card(struct mmc_host * host,u32 ocr,struct mmc_card * oldcard)
- Line: 1419

### mmc_sd_init_uhs_card
- Return type: static int
- Signature: mmc_sd_init_uhs_card(struct mmc_card * card)
- Line: 643

### mmc_sd_remove
- Return type: static void
- Signature: mmc_sd_remove(struct mmc_host * host)
- Line: 1741

### mmc_sd_resume
- Return type: static int
- Signature: mmc_sd_resume(struct mmc_host * host)
- Line: 1792

### mmc_sd_runtime_resume
- Return type: static int
- Signature: mmc_sd_runtime_resume(struct mmc_host * host)
- Line: 1819

### mmc_sd_runtime_suspend
- Return type: static int
- Signature: mmc_sd_runtime_suspend(struct mmc_host * host)
- Line: 1801

### mmc_sd_setup_card
- Return type: int
- Signature: mmc_sd_setup_card(struct mmc_host * host,struct mmc_card * card,bool reinit)
- Line: 943

### mmc_sd_suspend
- Return type: static int
- Signature: mmc_sd_suspend(struct mmc_host * host)
- Line: 1754

### mmc_sd_switch_hs
- Return type: int
- Signature: mmc_sd_switch_hs(struct mmc_card * card)
- Line: 380

### mmc_sd_use_tuning
- Return type: static bool
- Signature: mmc_sd_use_tuning(struct mmc_card * card)
- Line: 620

### sd_busy_poweroff_notify_cb
- Return type: static int
- Signature: sd_busy_poweroff_notify_cb(void * cb_data,bool * busy)
- Line: 1652

### sd_cache_enabled
- Return type: static bool
- Signature: sd_cache_enabled(struct mmc_host * host)
- Line: 1323

### sd_can_poweroff_notify
- Return type: static int
- Signature: sd_can_poweroff_notify(struct mmc_card * card)
- Line: 1647

### sd_enable_cache
- Return type: static int
- Signature: sd_enable_cache(struct mmc_card * card)
- Line: 1380

### sd_flush_cache
- Return type: static int
- Signature: sd_flush_cache(struct mmc_host * host)
- Line: 1328

### sd_get_host_max_current
- Return type: static u32
- Signature: sd_get_host_max_current(struct mmc_host * host)
- Line: 531

### sd_parse_ext_reg
- Return type: static int
- Signature: sd_parse_ext_reg(struct mmc_card * card,u8 * gen_info_buf,u16 * next_ext_addr)
- Line: 1205

### sd_parse_ext_reg_perf
- Return type: static int
- Signature: sd_parse_ext_reg_perf(struct mmc_card * card,u8 fno,u8 page,u16 offset)
- Line: 1156

### sd_parse_ext_reg_power
- Return type: static int
- Signature: sd_parse_ext_reg_power(struct mmc_card * card,u8 fno,u8 page,u16 offset)
- Line: 1114

### sd_poweroff_notify
- Return type: static int
- Signature: sd_poweroff_notify(struct mmc_card * card)
- Line: 1675

### sd_read_ext_reg
- Return type: static int
- Signature: sd_read_ext_reg(struct mmc_card * card,u8 fno,u8 page,u16 offset,u16 len,u8 * reg_buf)
- Line: 1094

### sd_read_ext_regs
- Return type: static int
- Signature: sd_read_ext_regs(struct mmc_card * card)
- Line: 1256

### sd_select_driver_type
- Return type: static int
- Signature: sd_select_driver_type(struct mmc_card * card,u8 * status)
- Line: 420

### sd_set_bus_speed_mode
- Return type: static int
- Signature: sd_set_bus_speed_mode(struct mmc_card * card,u8 * status)
- Line: 485

### sd_set_current_limit
- Return type: static int
- Signature: sd_set_current_limit(struct mmc_card * card,u8 * status)
- Line: 555

### sd_std_is_visible
- Return type: static umode_t
- Signature: sd_std_is_visible(struct kobject * kobj,struct attribute * attr,int index)
- Line: 795

### sd_update_bus_speed_mode
- Return type: static void
- Signature: sd_update_bus_speed_mode(struct mmc_card * card)
- Line: 452

### sd_write_ext_reg
- Return type: static int
- Signature: sd_write_ext_reg(struct mmc_card * card,u8 fno,u8 page,u16 offset,u8 reg_data)
- Line: 1034

## Structs (1)

### sd_busy_data
- Line: 63
- Members:
  - card: mmc_card *
  - reg_buf: u8 *

## Variables (9)

- static **mmc_sd_ops** : const struct mmc_bus_ops (line 1837)
- static **sd_au_size** : const unsigned int[] (line 53)
- static **sd_std_attrs** : attribute * [] (line 768)
- static **sd_std_group** : const struct attribute_group (line 815)
- **sd_type** : const struct device_type (line 821)
- static **taac_exp** : const unsigned int[] (line 44)
- static **taac_mant** : const unsigned int[] (line 48)
- static **tran_exp** : const unsigned int[] (line 34)
- static **tran_mant** : const unsigned char[] (line 39)

## Macros (3)

- **SD_POWEROFF_NOTIFY_TIMEOUT_MS** (line 60)
- **SD_WRITE_EXTR_SINGLE_TIMEOUT_MS** (line 61)
- **sdio_info_attr**(num) (line 750)
