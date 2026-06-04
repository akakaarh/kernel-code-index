# drivers/mmc/host/mmci_stm32_sdmmc.c

Subsystem: drivers/mmc

## Functions (24)

### _sdmmc_idma_prep_data
- Return type: static int
- Signature: _sdmmc_idma_prep_data(struct mmci_host * host,struct mmc_data * data)
- Line: 131

### mmci_sdmmc_set_clkreg
- Return type: static void
- Signature: mmci_sdmmc_set_clkreg(struct mmci_host * host,unsigned int desired)
- Line: 298

### mmci_sdmmc_set_pwrreg
- Return type: static void
- Signature: mmci_sdmmc_set_pwrreg(struct mmci_host * host,unsigned int pwr)
- Line: 360

### sdmmc_busy_complete
- Return type: static bool
- Signature: sdmmc_busy_complete(struct mmci_host * host,struct mmc_command * cmd,u32 status,u32 err_msk)
- Line: 438

### sdmmc_dlyb_mp15_enable
- Return type: static int
- Signature: sdmmc_dlyb_mp15_enable(struct sdmmc_dlyb * dlyb)
- Line: 480

### sdmmc_dlyb_mp15_input_ck
- Return type: static void
- Signature: sdmmc_dlyb_mp15_input_ck(struct sdmmc_dlyb * dlyb)
- Line: 351

### sdmmc_dlyb_mp15_prepare
- Return type: static int
- Signature: sdmmc_dlyb_mp15_prepare(struct mmci_host * host)
- Line: 504

### sdmmc_dlyb_mp15_set_cfg
- Return type: static int
- Signature: sdmmc_dlyb_mp15_set_cfg(struct sdmmc_dlyb * dlyb,int unit,int phase,bool sampler)
- Line: 487

### sdmmc_dlyb_mp25_enable
- Return type: static int
- Signature: sdmmc_dlyb_mp25_enable(struct sdmmc_dlyb * dlyb)
- Line: 537

### sdmmc_dlyb_mp25_prepare
- Return type: static int
- Signature: sdmmc_dlyb_mp25_prepare(struct mmci_host * host)
- Line: 568

### sdmmc_dlyb_mp25_set_cfg
- Return type: static int
- Signature: sdmmc_dlyb_mp25_set_cfg(struct sdmmc_dlyb * dlyb,int unit __maybe_unused,int phase,bool sampler __maybe_unused)
- Line: 551

### sdmmc_dlyb_phase_tuning
- Return type: static int
- Signature: sdmmc_dlyb_phase_tuning(struct mmci_host * host,u32 opcode)
- Line: 577

### sdmmc_execute_tuning
- Return type: static int
- Signature: sdmmc_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 622

### sdmmc_get_dctrl_cfg
- Return type: static u32
- Signature: sdmmc_get_dctrl_cfg(struct mmci_host * host)
- Line: 408

### sdmmc_idma_error
- Return type: static void
- Signature: sdmmc_idma_error(struct mmci_host * host)
- Line: 269

### sdmmc_idma_finalize
- Return type: static void
- Signature: sdmmc_idma_finalize(struct mmci_host * host,struct mmc_data * data)
- Line: 286

### sdmmc_idma_prep_data
- Return type: static int
- Signature: sdmmc_idma_prep_data(struct mmci_host * host,struct mmc_data * data,bool next)
- Line: 160

### sdmmc_idma_setup
- Return type: static int
- Signature: sdmmc_idma_setup(struct mmci_host * host)
- Line: 188

### sdmmc_idma_start
- Return type: static int
- Signature: sdmmc_idma_start(struct mmci_host * host,unsigned int * datactrl)
- Line: 220

### sdmmc_idma_unprep_data
- Return type: static void
- Signature: sdmmc_idma_unprep_data(struct mmci_host * host,struct mmc_data * data,int err)
- Line: 170

### sdmmc_idma_validate_data
- Return type: static int
- Signature: sdmmc_idma_validate_data(struct mmci_host * host,struct mmc_data * data)
- Line: 81

### sdmmc_post_sig_volt_switch
- Return type: static int
- Signature: sdmmc_post_sig_volt_switch(struct mmci_host * host,struct mmc_ios * ios)
- Line: 665

### sdmmc_pre_sig_volt_vswitch
- Return type: static void
- Signature: sdmmc_pre_sig_volt_vswitch(struct mmci_host * host)
- Line: 657

### sdmmc_variant_init
- Return type: void
- Signature: sdmmc_variant_init(struct mmci_host * host)
- Line: 724

## Structs (4)

### sdmmc_dlyb
- Line: 74
- Members:
  - idmalar: u32
  - idmabase: u32
  - idmasize: u32
  - sg_dma: dma_addr_t
  - sg_cpu: void *
  - bounce_dma_addr: dma_addr_t
  - bounce_buf: void *
  - use_bounce_buffer: bool
  - dlyb_enable: int (*)(struct sdmmc_dlyb * dlyb)
  - set_input_ck: void (*)(struct sdmmc_dlyb * dlyb)
  - tuning_prepare: int (*)(struct mmci_host * host)
  - set_cfg: int (*)(struct sdmmc_dlyb * dlyb,int unit __maybe_unused,int phase,bool sampler __maybe_unused)
  - base: void __iomem *
  - unit: u32
  - max: u32
  - ops: sdmmc_tuning_ops *

### sdmmc_idma
- Line: 56
- Members:
  - idmalar: u32
  - idmabase: u32
  - idmasize: u32
  - sg_dma: dma_addr_t
  - sg_cpu: void *
  - bounce_dma_addr: dma_addr_t
  - bounce_buf: void *
  - use_bounce_buffer: bool
  - dlyb_enable: int (*)(struct sdmmc_dlyb * dlyb)
  - set_input_ck: void (*)(struct sdmmc_dlyb * dlyb)
  - tuning_prepare: int (*)(struct mmci_host * host)
  - set_cfg: int (*)(struct sdmmc_dlyb * dlyb,int unit __maybe_unused,int phase,bool sampler __maybe_unused)
  - base: void __iomem *
  - unit: u32
  - max: u32
  - ops: sdmmc_tuning_ops *

### sdmmc_lli_desc
- Line: 50
- Members:
  - idmalar: u32
  - idmabase: u32
  - idmasize: u32
  - sg_dma: dma_addr_t
  - sg_cpu: void *
  - bounce_dma_addr: dma_addr_t
  - bounce_buf: void *
  - use_bounce_buffer: bool
  - dlyb_enable: int (*)(struct sdmmc_dlyb * dlyb)
  - set_input_ck: void (*)(struct sdmmc_dlyb * dlyb)
  - tuning_prepare: int (*)(struct mmci_host * host)
  - set_cfg: int (*)(struct sdmmc_dlyb * dlyb,int unit __maybe_unused,int phase,bool sampler __maybe_unused)
  - base: void __iomem *
  - unit: u32
  - max: u32
  - ops: sdmmc_tuning_ops *

### sdmmc_tuning_ops
- Line: 66
- Members:
  - idmalar: u32
  - idmabase: u32
  - idmasize: u32
  - sg_dma: dma_addr_t
  - sg_cpu: void *
  - bounce_dma_addr: dma_addr_t
  - bounce_buf: void *
  - use_bounce_buffer: bool
  - dlyb_enable: int (*)(struct sdmmc_dlyb * dlyb)
  - set_input_ck: void (*)(struct sdmmc_dlyb * dlyb)
  - tuning_prepare: int (*)(struct mmci_host * host)
  - set_cfg: int (*)(struct sdmmc_dlyb * dlyb,int unit __maybe_unused,int phase,bool sampler __maybe_unused)
  - base: void __iomem *
  - unit: u32
  - max: u32
  - ops: sdmmc_tuning_ops *

## Variables (3)

- static **dlyb_tuning_mp15_ops** : sdmmc_tuning_ops (line 711)
- static **dlyb_tuning_mp25_ops** : sdmmc_tuning_ops (line 718)
- static **sdmmc_variant_ops** : mmci_host_ops (line 695)

## Macros (25)

- **DLYBSD_ANTIGLITCH_EN** (line 42)
- **DLYBSD_BYP_CMD** (line 41)
- **DLYBSD_BYP_EN** (line 40)
- **DLYBSD_CR_EN** (line 37)
- **DLYBSD_CR_RXTAPSEL_MASK** (line 38)
- **DLYBSD_SR_LOCK** (line 45)
- **DLYBSD_SR_RXTAPSEL_ACK** (line 46)
- **DLYBSD_TAPSEL_NB** (line 39)
- **DLYBSD_TIMEOUT_1S_IN_US** (line 48)
- **DLYB_CFGR** (line 23)
- **DLYB_CFGR_LNGF** (line 27)
- **DLYB_CFGR_LNG_MASK** (line 26)
- **DLYB_CFGR_SEL_MASK** (line 24)
- **DLYB_CFGR_SEL_MAX** (line 30)
- **DLYB_CFGR_UNIT_MASK** (line 25)
- **DLYB_CFGR_UNIT_MAX** (line 31)
- **DLYB_CR** (line 19)
- **DLYB_CR_DEN** (line 20)
- **DLYB_CR_SEN** (line 21)
- **DLYB_LNG_TIMEOUT_US** (line 33)
- **DLYB_NB_DELAY** (line 29)
- **SDMMC_LLI_BUF_LEN** (line 17)
- **SDMMC_VSWEND_TIMEOUT_US** (line 34)
- **SYSCFG_DLYBSD_CR** (line 36)
- **SYSCFG_DLYBSD_SR** (line 44)
