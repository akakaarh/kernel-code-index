# drivers/mmc/core/mmc.c

Subsystem: drivers/mmc

## Functions (50)

### __mmc_select_powerclass
- Return type: static int
- Signature: __mmc_select_powerclass(struct mmc_card * card,unsigned int bus_width)
- Line: 905

### _mmc_cache_enabled
- Return type: static bool
- Signature: _mmc_cache_enabled(struct mmc_host * host)
- Line: 2106

### _mmc_flush_cache
- Return type: static int
- Signature: _mmc_flush_cache(struct mmc_host * host)
- Line: 2115

### _mmc_handle_undervoltage
- Return type: static int
- Signature: _mmc_handle_undervoltage(struct mmc_host * host)
- Line: 2353

### _mmc_hw_reset
- Return type: static int
- Signature: _mmc_hw_reset(struct mmc_host * host)
- Line: 2306

### _mmc_resume
- Return type: static int
- Signature: _mmc_resume(struct mmc_host * host)
- Line: 2209

### _mmc_suspend
- Return type: static int
- Signature: _mmc_suspend(struct mmc_host * host,enum mmc_poweroff_type pm_type)
- Line: 2135

### mmc_alive
- Return type: static int
- Signature: mmc_alive(struct mmc_host * host)
- Line: 2074

### mmc_attach_mmc
- Return type: int
- Signature: mmc_attach_mmc(struct mmc_host * host)
- Line: 2398

### mmc_card_can_poweroff_notify
- Return type: static bool
- Signature: mmc_card_can_poweroff_notify(const struct mmc_card * card)
- Line: 2029

### mmc_card_can_reset
- Return type: static bool
- Signature: mmc_card_can_reset(struct mmc_card * card)
- Line: 2298

### mmc_card_can_sleep
- Return type: static bool
- Signature: mmc_card_can_sleep(struct mmc_card * card)
- Line: 1971

### mmc_compare_ext_csds
- Return type: static int
- Signature: mmc_compare_ext_csds(struct mmc_card * card,unsigned bus_width)
- Line: 729

### mmc_decode_cid
- Return type: static int
- Signature: mmc_decode_cid(struct mmc_card * card)
- Line: 65

### mmc_decode_csd
- Return type: static int
- Signature: mmc_decode_csd(struct mmc_card * card)
- Line: 150

### mmc_decode_ext_csd
- Return type: static int
- Signature: mmc_decode_ext_csd(struct mmc_card * card,u8 * ext_csd)
- Line: 379

### mmc_detect
- Return type: static void
- Signature: mmc_detect(struct mmc_host * host)
- Line: 2082

### mmc_dsr_show
- Return type: static ssize_t
- Signature: mmc_dsr_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 848

### mmc_fwrev_show
- Return type: static ssize_t
- Signature: mmc_fwrev_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 833

### mmc_host_can_poweroff_notify
- Return type: static bool
- Signature: mmc_host_can_poweroff_notify(const struct mmc_host * host,enum mmc_poweroff_type pm_type)
- Line: 2036

### mmc_hs200_to_hs400
- Return type: int
- Signature: mmc_hs200_to_hs400(struct mmc_card * card)
- Line: 1276

### mmc_hs200_tuning
- Return type: static int
- Signature: mmc_hs200_tuning(struct mmc_card * card)
- Line: 1595

### mmc_hs400_to_hs200
- Return type: int
- Signature: mmc_hs400_to_hs200(struct mmc_card * card)
- Line: 1281

### mmc_init_card
- Return type: static int
- Signature: mmc_init_card(struct mmc_host * host,u32 ocr,struct mmc_card * oldcard)
- Line: 1617

### mmc_manage_enhanced_area
- Return type: static void
- Signature: mmc_manage_enhanced_area(struct mmc_card * card,u8 * ext_csd)
- Line: 269

### mmc_manage_gp_partitions
- Return type: static void
- Signature: mmc_manage_gp_partitions(struct mmc_card * card,u8 * ext_csd)
- Line: 330

### mmc_part_add
- Return type: static void
- Signature: mmc_part_add(struct mmc_card * card,u64 size,unsigned int part_cfg,char * name,int idx,bool ro,int area_type)
- Line: 318

### mmc_poweroff_notify
- Return type: static int
- Signature: mmc_poweroff_notify(struct mmc_card * card,unsigned int notify_type)
- Line: 2049

### mmc_read_ext_csd
- Return type: static int
- Signature: mmc_read_ext_csd(struct mmc_card * card)
- Line: 691

### mmc_remove
- Return type: static void
- Signature: mmc_remove(struct mmc_host * host)
- Line: 2178

### mmc_resume
- Return type: static int
- Signature: mmc_resume(struct mmc_host * host)
- Line: 2259

### mmc_runtime_resume
- Return type: static int
- Signature: mmc_runtime_resume(struct mmc_host * host)
- Line: 2286

### mmc_runtime_suspend
- Return type: static int
- Signature: mmc_runtime_suspend(struct mmc_host * host)
- Line: 2268

### mmc_select_bus_width
- Return type: static int
- Signature: mmc_select_bus_width(struct mmc_card * card)
- Line: 1022

### mmc_select_card_type
- Return type: static void
- Signature: mmc_select_card_type(struct mmc_card * card)
- Line: 203

### mmc_select_driver_type
- Return type: static void
- Signature: mmc_select_driver_type(struct mmc_card * card)
- Line: 1356

### mmc_select_hs
- Return type: static int
- Signature: mmc_select_hs(struct mmc_card * card)
- Line: 1093

### mmc_select_hs200
- Return type: static int
- Signature: mmc_select_hs200(struct mmc_card * card)
- Line: 1478

### mmc_select_hs400
- Return type: static int
- Signature: mmc_select_hs400(struct mmc_card * card)
- Line: 1181

### mmc_select_hs400es
- Return type: static int
- Signature: mmc_select_hs400es(struct mmc_card * card)
- Line: 1378

### mmc_select_hs_ddr
- Return type: static int
- Signature: mmc_select_hs_ddr(struct mmc_card * card)
- Line: 1111

### mmc_select_powerclass
- Return type: static int
- Signature: mmc_select_powerclass(struct mmc_card * card)
- Line: 968

### mmc_select_timing
- Return type: static int
- Signature: mmc_select_timing(struct mmc_card * card)
- Line: 1555

### mmc_set_bus_speed
- Return type: static void
- Signature: mmc_set_bus_speed(struct mmc_card * card)
- Line: 1002

### mmc_set_erase_size
- Return type: static void
- Signature: mmc_set_erase_size(struct mmc_card * card)
- Line: 126

### mmc_set_wp_grp_size
- Return type: static void
- Signature: mmc_set_wp_grp_size(struct mmc_card * card)
- Line: 137

### mmc_shutdown
- Return type: static int
- Signature: mmc_shutdown(struct mmc_host * host)
- Line: 2230

### mmc_sleep
- Return type: static int
- Signature: mmc_sleep(struct mmc_host * host)
- Line: 1984

### mmc_sleep_busy_cb
- Return type: static int
- Signature: mmc_sleep_busy_cb(void * cb_data,bool * busy)
- Line: 1976

### mmc_suspend
- Return type: static int
- Signature: mmc_suspend(struct mmc_host * host)
- Line: 2192

## Enums (1)

### mmc_poweroff_type
- Line: 36

## Variables (7)

- static **mmc_ops** : const struct mmc_bus_ops (line 2380)
- static **mmc_std_attrs** : attribute * [] (line 864)
- static **mmc_type** : const struct device_type (line 895)
- static **taac_exp** : const unsigned int[] (line 53)
- static **taac_mant** : const unsigned int[] (line 57)
- static **tran_exp** : const unsigned int[] (line 43)
- static **tran_mant** : const unsigned char[] (line 48)

## Macros (4)

- **CACHE_FLUSH_TIMEOUT_MS** (line 34)
- **DEFAULT_CMD6_TIMEOUT_MS** (line 32)
- **MIN_CACHE_EN_TIMEOUT_MS** (line 33)
- **MMC_MIN_PART_SWITCH_TIME** (line 374)
