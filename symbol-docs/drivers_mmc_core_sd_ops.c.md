# drivers/mmc/core/sd_ops.c

Subsystem: drivers/mmc

## Functions (13)

### __mmc_send_if_cond
- Return type: static int
- Signature: __mmc_send_if_cond(struct mmc_host * host,u32 ocr,u8 pcie_bits,u32 * resp)
- Line: 215

### mmc_app_cmd
- Return type: int
- Signature: mmc_app_cmd(struct mmc_host * host,struct mmc_card * card)
- Line: 37

### mmc_app_sd_status
- Return type: int
- Signature: mmc_app_sd_status(struct mmc_card * card,void * ssr)
- Line: 380

### mmc_app_send_scr
- Return type: int
- Signature: mmc_app_send_scr(struct mmc_card * card)
- Line: 309

### mmc_app_set_bus_width
- Return type: int
- Signature: mmc_app_set_bus_width(struct mmc_card * card,int width)
- Line: 121

### mmc_sd_switch
- Return type: int
- Signature: mmc_sd_switch(struct mmc_card * card,bool mode,int group,u8 value,u8 * resp)
- Line: 363

### mmc_send_app_op_cond
- Return type: int
- Signature: mmc_send_app_op_cond(struct mmc_host * host,u32 ocr,u32 * rocr)
- Line: 172

### mmc_send_ext_addr
- Return type: int
- Signature: mmc_send_ext_addr(struct mmc_host * host,u32 addr)
- Line: 201

### mmc_send_if_cond
- Return type: int
- Signature: mmc_send_if_cond(struct mmc_host * host,u32 ocr)
- Line: 250

### mmc_send_if_cond_pcie
- Return type: int
- Signature: mmc_send_if_cond_pcie(struct mmc_host * host,u32 ocr)
- Line: 255

### mmc_send_relative_addr
- Return type: int
- Signature: mmc_send_relative_addr(struct mmc_host * host,unsigned int * rca)
- Line: 291

### mmc_wait_for_app_cmd
- Return type: static int
- Signature: mmc_wait_for_app_cmd(struct mmc_host * host,struct mmc_card * card,struct mmc_command * cmd)
- Line: 76

### sd_app_op_cond_cb
- Return type: static int
- Signature: sd_app_op_cond_cb(void * cb_data,bool * busy)
- Line: 142

## Structs (1)

### sd_app_op_cond_busy_data
- Line: 31
- Members:
  - host: mmc_host *
  - ocr: u32
  - cmd: mmc_command *

## Macros (2)

- **SD_APP_OP_COND_PERIOD_US** (line 28)
- **SD_APP_OP_COND_TIMEOUT_MS** (line 29)
