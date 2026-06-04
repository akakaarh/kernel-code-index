# drivers/mmc/core/sdio.c

Subsystem: drivers/mmc

## Functions (29)

### host_drive_to_sdio_drive
- Return type: static unsigned char
- Signature: host_drive_to_sdio_drive(int host_strength)
- Line: 466

### mmc_attach_sdio
- Return type: int
- Signature: mmc_attach_sdio(struct mmc_host * host)
- Line: 1212

### mmc_sdio_alive
- Return type: static int
- Signature: mmc_sdio_alive(struct mmc_host * host)
- Line: 946

### mmc_sdio_detect
- Return type: static void
- Signature: mmc_sdio_detect(struct mmc_host * host)
- Line: 958

### mmc_sdio_get_max_clock
- Return type: static unsigned
- Signature: mmc_sdio_get_max_clock(struct mmc_card * card)
- Line: 442

### mmc_sdio_hw_reset
- Return type: static int
- Signature: mmc_sdio_hw_reset(struct mmc_host * host)
- Line: 1157

### mmc_sdio_init_card
- Return type: static int
- Signature: mmc_sdio_init_card(struct mmc_host * host,u32 ocr,struct mmc_card * oldcard)
- Line: 660

### mmc_sdio_init_uhs_card
- Return type: static int
- Signature: mmc_sdio_init_uhs_card(struct mmc_card * card)
- Line: 593

### mmc_sdio_pre_init
- Return type: static int
- Signature: mmc_sdio_pre_init(struct mmc_host * host,u32 ocr,struct mmc_card * card)
- Line: 625

### mmc_sdio_pre_suspend
- Return type: static int
- Signature: mmc_sdio_pre_suspend(struct mmc_host * host)
- Line: 1008

### mmc_sdio_reinit_card
- Return type: static int
- Signature: mmc_sdio_reinit_card(struct mmc_host * host)
- Line: 914

### mmc_sdio_remove
- Return type: static void
- Signature: mmc_sdio_remove(struct mmc_host * host)
- Line: 928

### mmc_sdio_resume
- Return type: static int
- Signature: mmc_sdio_resume(struct mmc_host * host)
- Line: 1071

### mmc_sdio_runtime_resume
- Return type: static int
- Signature: mmc_sdio_runtime_resume(struct mmc_host * host)
- Line: 1138

### mmc_sdio_runtime_suspend
- Return type: static int
- Signature: mmc_sdio_runtime_suspend(struct mmc_host * host)
- Line: 1128

### mmc_sdio_suspend
- Return type: static int
- Signature: mmc_sdio_suspend(struct mmc_host * host)
- Line: 1046

### mmc_sdio_sw_reset
- Return type: static int
- Signature: mmc_sdio_sw_reset(struct mmc_host * host)
- Line: 1183

### mmc_sdio_switch_hs
- Return type: static int
- Signature: mmc_sdio_switch_hs(struct mmc_card * card,int enable)
- Line: 397

### sdio_disable_4bit_bus
- Return type: static int
- Signature: sdio_disable_4bit_bus(struct mmc_card * card)
- Line: 348

### sdio_disable_cd
- Return type: static int
- Signature: sdio_disable_cd(struct mmc_card * card)
- Line: 297

### sdio_disable_wide
- Return type: static int
- Signature: sdio_disable_wide(struct mmc_card * card)
- Line: 318

### sdio_enable_4bit_bus
- Return type: static int
- Signature: sdio_enable_4bit_bus(struct mmc_card * card)
- Line: 370

### sdio_enable_hs
- Return type: static int
- Signature: sdio_enable_hs(struct mmc_card * card)
- Line: 427

### sdio_enable_wide
- Return type: static int
- Signature: sdio_enable_wide(struct mmc_card * card)
- Line: 261

### sdio_init_func
- Return type: static int
- Signature: sdio_init_func(struct mmc_card * card,unsigned int fn)
- Line: 103

### sdio_read_cccr
- Return type: static int
- Signature: sdio_read_cccr(struct mmc_card * card,u32 ocr)
- Line: 144

### sdio_read_fbr
- Return type: static int
- Signature: sdio_read_fbr(struct sdio_func * func)
- Line: 73

### sdio_select_driver_type
- Return type: static void
- Signature: sdio_select_driver_type(struct mmc_card * card)
- Line: 482

### sdio_set_bus_speed_mode
- Return type: static int
- Signature: sdio_set_bus_speed_mode(struct mmc_card * card)
- Line: 519

## Variables (3)

- static **mmc_sdio_ops** : const struct mmc_bus_ops (line 1195)
- static **sdio_std_attrs** : attribute * [] (line 55)
- static **sdio_type** : const struct device_type (line 69)

## Macros (1)

- **sdio_info_attr**(num) (line 37)
