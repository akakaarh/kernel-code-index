# drivers/mmc/core/sdio_ops.c

Subsystem: drivers/mmc

## Functions (5)

### mmc_io_rw_direct
- Return type: int
- Signature: mmc_io_rw_direct(struct mmc_card * card,int write,unsigned fn,unsigned addr,u8 in,u8 * out)
- Line: 108

### mmc_io_rw_direct_host
- Return type: static int
- Signature: mmc_io_rw_direct_host(struct mmc_host * host,int write,unsigned fn,unsigned addr,u8 in,u8 * out)
- Line: 62

### mmc_io_rw_extended
- Return type: int
- Signature: mmc_io_rw_extended(struct mmc_card * card,int write,unsigned fn,unsigned addr,int incr_addr,u8 * buf,unsigned blocks,unsigned blksz)
- Line: 114

### mmc_send_io_op_cond
- Return type: int
- Signature: mmc_send_io_op_cond(struct mmc_host * host,u32 ocr,u32 * rocr)
- Line: 18

### sdio_reset
- Return type: int
- Signature: sdio_reset(struct mmc_host * host)
- Line: 202
