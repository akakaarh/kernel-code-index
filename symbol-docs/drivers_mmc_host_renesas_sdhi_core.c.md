# drivers/mmc/host/renesas_sdhi_core.c

Subsystem: drivers/mmc

## Functions (43)

### renesas_sdhi_adjust_hs400_mode_disable
- Return type: static void
- Signature: renesas_sdhi_adjust_hs400_mode_disable(struct tmio_mmc_host * host)
- Line: 527

### renesas_sdhi_adjust_hs400_mode_enable
- Return type: static void
- Signature: renesas_sdhi_adjust_hs400_mode_enable(struct tmio_mmc_host * host)
- Line: 504

### renesas_sdhi_auto_correction
- Return type: static bool
- Signature: renesas_sdhi_auto_correction(struct tmio_mmc_host * host)
- Line: 811

### renesas_sdhi_card_busy
- Return type: static int
- Signature: renesas_sdhi_card_busy(struct mmc_host * mmc)
- Line: 251

### renesas_sdhi_check_scc_error
- Return type: static bool
- Signature: renesas_sdhi_check_scc_error(struct tmio_mmc_host * host,struct mmc_request * mrq)
- Line: 825

### renesas_sdhi_clk_disable
- Return type: static void
- Signature: renesas_sdhi_clk_disable(struct tmio_mmc_host * host)
- Line: 244

### renesas_sdhi_clk_enable
- Return type: static int
- Signature: renesas_sdhi_clk_enable(struct tmio_mmc_host * host)
- Line: 97

### renesas_sdhi_clk_update
- Return type: static unsigned int
- Signature: renesas_sdhi_clk_update(struct tmio_mmc_host * host,unsigned int wanted_clock)
- Line: 128

### renesas_sdhi_disable_scc
- Return type: static void
- Signature: renesas_sdhi_disable_scc(struct mmc_host * mmc)
- Line: 450

### renesas_sdhi_enable_dma
- Return type: static void
- Signature: renesas_sdhi_enable_dma(struct tmio_mmc_host * host,bool enable)
- Line: 950

### renesas_sdhi_execute_tuning
- Return type: static int
- Signature: renesas_sdhi_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 702

### renesas_sdhi_fixup_request
- Return type: static void
- Signature: renesas_sdhi_fixup_request(struct tmio_mmc_host * host,struct mmc_request * mrq)
- Line: 943

### renesas_sdhi_gen3_get_cycles
- Return type: static unsigned int
- Signature: renesas_sdhi_gen3_get_cycles(struct tmio_mmc_host * host)
- Line: 627

### renesas_sdhi_hs400_complete
- Return type: static void
- Signature: renesas_sdhi_hs400_complete(struct mmc_host * mmc)
- Line: 389

### renesas_sdhi_init_card
- Return type: static void
- Signature: renesas_sdhi_init_card(struct mmc_host * mmc,struct mmc_card * card)
- Line: 862

### renesas_sdhi_init_tuning
- Return type: static unsigned int
- Signature: renesas_sdhi_init_tuning(struct tmio_mmc_host * host)
- Line: 353

### renesas_sdhi_manual_correction
- Return type: static bool
- Signature: renesas_sdhi_manual_correction(struct tmio_mmc_host * host,bool use_4tap)
- Line: 744

### renesas_sdhi_multi_io_quirk
- Return type: static int
- Signature: renesas_sdhi_multi_io_quirk(struct mmc_card * card,unsigned int direction,int blk_size)
- Line: 925

### renesas_sdhi_prepare_hs400_tuning
- Return type: static int
- Signature: renesas_sdhi_prepare_hs400_tuning(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 564

### renesas_sdhi_probe
- Return type: int
- Signature: renesas_sdhi_probe(struct platform_device * pdev,const struct tmio_mmc_dma_ops * dma_ops,const struct renesas_sdhi_of_data * of_data,const struct renesas_sdhi_quirks * quirks)
- Line: 1055

### renesas_sdhi_regulator_disable
- Return type: static int
- Signature: renesas_sdhi_regulator_disable(struct regulator_dev * rdev)
- Line: 963

### renesas_sdhi_regulator_enable
- Return type: static int
- Signature: renesas_sdhi_regulator_enable(struct regulator_dev * rdev)
- Line: 975

### renesas_sdhi_regulator_get_voltage
- Return type: static int
- Signature: renesas_sdhi_regulator_get_voltage(struct regulator_dev * rdev)
- Line: 997

### renesas_sdhi_regulator_is_enabled
- Return type: static int
- Signature: renesas_sdhi_regulator_is_enabled(struct regulator_dev * rdev)
- Line: 987

### renesas_sdhi_regulator_list_voltage
- Return type: static int
- Signature: renesas_sdhi_regulator_list_voltage(struct regulator_dev * rdev,unsigned int selector)
- Line: 1027

### renesas_sdhi_regulator_set_voltage
- Return type: static int
- Signature: renesas_sdhi_regulator_set_voltage(struct regulator_dev * rdev,int min_uV,int max_uV,unsigned int * selector)
- Line: 1007

### renesas_sdhi_remove
- Return type: void
- Signature: renesas_sdhi_remove(struct platform_device * pdev)
- Line: 1318

### renesas_sdhi_reset
- Return type: static void
- Signature: renesas_sdhi_reset(struct tmio_mmc_host * host,bool preserve)
- Line: 584

### renesas_sdhi_reset_hs400_mode
- Return type: static void
- Signature: renesas_sdhi_reset_hs400_mode(struct tmio_mmc_host * host,struct renesas_sdhi * priv)
- Line: 540

### renesas_sdhi_resume
- Return type: int
- Signature: renesas_sdhi_resume(struct device * dev)
- Line: 1345

### renesas_sdhi_scc_reset
- Return type: static void
- Signature: renesas_sdhi_scc_reset(struct tmio_mmc_host * host,struct renesas_sdhi * priv)
- Line: 572

### renesas_sdhi_sdbuf_width
- Return type: static void
- Signature: renesas_sdhi_sdbuf_width(struct tmio_mmc_host * host,int width)
- Line: 65

### renesas_sdhi_sdio_irq
- Return type: static void
- Signature: renesas_sdhi_sdio_irq(struct tmio_mmc_host * host)
- Line: 877

### renesas_sdhi_select_tuning
- Return type: static int
- Signature: renesas_sdhi_select_tuning(struct tmio_mmc_host * host)
- Line: 638

### renesas_sdhi_set_clock
- Return type: static void
- Signature: renesas_sdhi_set_clock(struct tmio_mmc_host * host,unsigned int new_clock)
- Line: 193

### renesas_sdhi_start_signal_voltage_switch
- Return type: static int
- Signature: renesas_sdhi_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 259

### renesas_sdhi_suspend
- Return type: int
- Signature: renesas_sdhi_suspend(struct device * dev)
- Line: 1327

### renesas_sdhi_wait_idle
- Return type: static int
- Signature: renesas_sdhi_wait_idle(struct tmio_mmc_host * host,u32 bit)
- Line: 884

### renesas_sdhi_write16_hook
- Return type: static int
- Signature: renesas_sdhi_write16_hook(struct tmio_mmc_host * host,int addr)
- Line: 902

### sd_scc_read32
- Return type: static u32
- Signature: sd_scc_read32(struct tmio_mmc_host * host,struct renesas_sdhi * priv,int addr)
- Line: 340

### sd_scc_tmpport_read32
- Return type: static u32
- Signature: sd_scc_tmpport_read32(struct tmio_mmc_host * host,struct renesas_sdhi * priv,u32 addr)
- Line: 472

### sd_scc_tmpport_write32
- Return type: static void
- Signature: sd_scc_tmpport_write32(struct tmio_mmc_host * host,struct renesas_sdhi * priv,u32 addr,u32 val)
- Line: 488

### sd_scc_write32
- Return type: static void
- Signature: sd_scc_write32(struct tmio_mmc_host * host,struct renesas_sdhi * priv,int addr,u32 val)
- Line: 346

## Variables (3)

- static **renesas_sdhi_regulator_voltage_ops** : const struct regulator_ops (line 1036)
- static **renesas_sdhi_vqmmc_regulator** : const struct regulator_desc (line 1045)
- static **renesas_sdhi_vqmmc_voltages** : const unsigned int[] (line 959)

## Macros (48)

- **CTL_HOST_MODE** (line 46)
- **HOST_MODE_GEN2_SDR104_WMODE** (line 48)
- **HOST_MODE_GEN2_SDR50_WMODE** (line 47)
- **HOST_MODE_GEN3_16BIT** (line 52)
- **HOST_MODE_GEN3_32BIT** (line 53)
- **HOST_MODE_GEN3_64BIT** (line 54)
- **HOST_MODE_GEN3_BUSWIDTH** (line 50)
- **HOST_MODE_GEN3_WMODE** (line 49)
- **SDHI_GEN3_MMC0_ADDR** (line 63)
- **SDHI_VER_GEN2_SDR104** (line 59)
- **SDHI_VER_GEN2_SDR50** (line 56)
- **SDHI_VER_GEN3_SD** (line 60)
- **SDHI_VER_GEN3_SDMMC** (line 61)
- **SDHI_VER_RZ_A1** (line 57)
- **SH_MOBILE_SDHI_MIN_TAP_ROW** (line 636)
- **SH_MOBILE_SDHI_SCC_CKSEL** (line 297)
- **SH_MOBILE_SDHI_SCC_CKSEL_DTSEL** (line 312)
- **SH_MOBILE_SDHI_SCC_DT2FF** (line 296)
- **SH_MOBILE_SDHI_SCC_DTCNTL** (line 294)
- **SH_MOBILE_SDHI_SCC_DTCNTL_TAPEN** (line 308)
- **SH_MOBILE_SDHI_SCC_DTCNTL_TAPNUM_MASK** (line 310)
- **SH_MOBILE_SDHI_SCC_DTCNTL_TAPNUM_SHIFT** (line 309)
- **SH_MOBILE_SDHI_SCC_RVSCNTL** (line 298)
- **SH_MOBILE_SDHI_SCC_RVSCNTL_RVSEN** (line 314)
- **SH_MOBILE_SDHI_SCC_RVSREQ** (line 299)
- **SH_MOBILE_SDHI_SCC_RVSREQ_REQTAPDOWN** (line 316)
- **SH_MOBILE_SDHI_SCC_RVSREQ_REQTAPUP** (line 317)
- **SH_MOBILE_SDHI_SCC_RVSREQ_RVSERR** (line 318)
- **SH_MOBILE_SDHI_SCC_SMPCMP** (line 300)
- **SH_MOBILE_SDHI_SCC_SMPCMP_CMD_ERR** (line 322)
- **SH_MOBILE_SDHI_SCC_SMPCMP_CMD_REQDOWN** (line 320)
- **SH_MOBILE_SDHI_SCC_SMPCMP_CMD_REQUP** (line 321)
- **SH_MOBILE_SDHI_SCC_TAPSET** (line 295)
- **SH_MOBILE_SDHI_SCC_TMPPORT2** (line 301)
- **SH_MOBILE_SDHI_SCC_TMPPORT2_HS400EN** (line 325)
- **SH_MOBILE_SDHI_SCC_TMPPORT2_HS400OSEL** (line 324)
- **SH_MOBILE_SDHI_SCC_TMPPORT3** (line 302)
- **SH_MOBILE_SDHI_SCC_TMPPORT4** (line 303)
- **SH_MOBILE_SDHI_SCC_TMPPORT4_DLL_ACC_START** (line 328)
- **SH_MOBILE_SDHI_SCC_TMPPORT5** (line 304)
- **SH_MOBILE_SDHI_SCC_TMPPORT5_DLL_ADR_MASK** (line 333)
- **SH_MOBILE_SDHI_SCC_TMPPORT5_DLL_RW_SEL_R** (line 331)
- **SH_MOBILE_SDHI_SCC_TMPPORT5_DLL_RW_SEL_W** (line 332)
- **SH_MOBILE_SDHI_SCC_TMPPORT6** (line 305)
- **SH_MOBILE_SDHI_SCC_TMPPORT7** (line 306)
- **SH_MOBILE_SDHI_SCC_TMPPORT_CALIB_CODE_MASK** (line 337)
- **SH_MOBILE_SDHI_SCC_TMPPORT_DISABLE_WP_CODE** (line 336)
- **SH_MOBILE_SDHI_SCC_TMPPORT_MANUAL_MODE** (line 338)
