# drivers/mmc/core/sd_uhs2.c

Subsystem: drivers/mmc

## Functions (27)

### _mmc_sd_uhs2_resume
- Return type: static int
- Signature: _mmc_sd_uhs2_resume(struct mmc_host * host)
- Line: 1082

### _sd_uhs2_suspend
- Return type: static int
- Signature: _sd_uhs2_suspend(struct mmc_host * host)
- Line: 1045

### mmc_attach_sd_uhs2
- Return type: int
- Signature: mmc_attach_sd_uhs2(struct mmc_host * host)
- Line: 1207

### mmc_uhs2_prepare_cmd
- Return type: void
- Signature: mmc_uhs2_prepare_cmd(struct mmc_host * host,struct mmc_request * mrq)
- Line: 1245

### sd_uhs2_alive
- Return type: static int
- Signature: sd_uhs2_alive(struct mmc_host * host)
- Line: 1022

### sd_uhs2_attach
- Return type: static int
- Signature: sd_uhs2_attach(struct mmc_host * host)
- Line: 1158

### sd_uhs2_cmd_assemble
- Return type: static void
- Signature: sd_uhs2_cmd_assemble(struct mmc_command * cmd,struct uhs2_command * uhs2_cmd,u8 plen,u8 resp_len)
- Line: 122

### sd_uhs2_config_read
- Return type: static int
- Signature: sd_uhs2_config_read(struct mmc_host * host,struct mmc_card * card)
- Line: 279

### sd_uhs2_config_write
- Return type: static int
- Signature: sd_uhs2_config_write(struct mmc_host * host,struct mmc_card * card)
- Line: 467

### sd_uhs2_detect
- Return type: static void
- Signature: sd_uhs2_detect(struct mmc_host * host)
- Line: 1027

### sd_uhs2_dev_init
- Return type: static int
- Signature: sd_uhs2_dev_init(struct mmc_host * host)
- Line: 137

### sd_uhs2_enum
- Return type: static int
- Signature: sd_uhs2_enum(struct mmc_host * host,u32 * node_id)
- Line: 226

### sd_uhs2_go_dormant
- Return type: static int
- Signature: sd_uhs2_go_dormant(struct mmc_host * host,u32 node_id)
- Line: 672

### sd_uhs2_go_dormant_state
- Return type: static int
- Signature: sd_uhs2_go_dormant_state(struct mmc_host * host,u32 node_id)
- Line: 759

### sd_uhs2_hw_reset
- Return type: static int
- Signature: sd_uhs2_hw_reset(struct mmc_host * host)
- Line: 1137

### sd_uhs2_init_card
- Return type: static int
- Signature: sd_uhs2_init_card(struct mmc_host * host,struct mmc_card * oldcard)
- Line: 805

### sd_uhs2_legacy_init
- Return type: static int
- Signature: sd_uhs2_legacy_init(struct mmc_host * host,struct mmc_card * card,bool reinit)
- Line: 863

### sd_uhs2_phy_init
- Return type: static int
- Signature: sd_uhs2_phy_init(struct mmc_host * host)
- Line: 88

### sd_uhs2_power_off
- Return type: static int
- Signature: sd_uhs2_power_off(struct mmc_host * host)
- Line: 62

### sd_uhs2_power_up
- Return type: static int
- Signature: sd_uhs2_power_up(struct mmc_host * host)
- Line: 49

### sd_uhs2_reinit
- Return type: static int
- Signature: sd_uhs2_reinit(struct mmc_host * host)
- Line: 996

### sd_uhs2_remove
- Return type: static void
- Signature: sd_uhs2_remove(struct mmc_host * host)
- Line: 1016

### sd_uhs2_resume
- Return type: static int
- Signature: sd_uhs2_resume(struct mmc_host * host)
- Line: 1103

### sd_uhs2_runtime_resume
- Return type: static int
- Signature: sd_uhs2_runtime_resume(struct mmc_host * host)
- Line: 1126

### sd_uhs2_runtime_suspend
- Return type: static int
- Signature: sd_uhs2_runtime_suspend(struct mmc_host * host)
- Line: 1112

### sd_uhs2_suspend
- Return type: static int
- Signature: sd_uhs2_suspend(struct mmc_host * host)
- Line: 1065

### sd_uhs2_wait_active_state_cb
- Return type: static int
- Signature: sd_uhs2_wait_active_state_cb(void * cb_data,bool * busy)
- Line: 740

## Structs (1)

### sd_uhs2_wait_active_state_data
- Line: 44
- Members:
  - host: mmc_host *
  - cmd: mmc_command *

## Variables (2)

- static **sd_uhs2_freqs** : const unsigned int[] (line 42)
- static **sd_uhs2_ops** : const struct mmc_bus_ops (line 1146)

## Macros (2)

- **UHS2_WAIT_CFG_COMPLETE_PERIOD_US** (line 39)
- **UHS2_WAIT_CFG_COMPLETE_TIMEOUT_MS** (line 40)
