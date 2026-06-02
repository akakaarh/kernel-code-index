# drivers/i2c/busses/i2c-xgene-slimpro.c

Subsystem: drivers/i2c

## Functions (14)

### slimpro_i2c_blkrd
- Return type: static int
- Signature: slimpro_i2c_blkrd(struct slimpro_i2c_dev * ctx,u32 chip,u32 addr,u32 addrlen,u32 protocol,u32 readlen,u32 with_data_len,void * data)
- Line: 263

### slimpro_i2c_blkwr
- Return type: static int
- Signature: slimpro_i2c_blkwr(struct slimpro_i2c_dev * ctx,u32 chip,u32 addr,u32 addrlen,u32 protocol,u32 writelen,void * data)
- Line: 295

### slimpro_i2c_pcc_rx_cb
- Return type: static void
- Signature: slimpro_i2c_pcc_rx_cb(struct mbox_client * cl,void * msg)
- Line: 146

### slimpro_i2c_pcc_tx_prepare
- Return type: static void
- Signature: slimpro_i2c_pcc_tx_prepare(struct slimpro_i2c_dev * ctx,u32 * msg)
- Line: 169

### slimpro_i2c_rd
- Return type: static int
- Signature: slimpro_i2c_rd(struct slimpro_i2c_dev * ctx,u32 chip,u32 addr,u32 addrlen,u32 protocol,u32 readlen,u32 * data)
- Line: 235

### slimpro_i2c_rx_cb
- Return type: static void
- Signature: slimpro_i2c_rx_cb(struct mbox_client * cl,void * mssg)
- Line: 129

### slimpro_i2c_send_msg
- Return type: static int
- Signature: slimpro_i2c_send_msg(struct slimpro_i2c_dev * ctx,u32 * msg,u32 * data)
- Line: 207

### slimpro_i2c_wr
- Return type: static int
- Signature: slimpro_i2c_wr(struct slimpro_i2c_dev * ctx,u32 chip,u32 addr,u32 addrlen,u32 protocol,u32 writelen,u32 data)
- Line: 249

### start_i2c_msg_xfer
- Return type: static int
- Signature: start_i2c_msg_xfer(struct slimpro_i2c_dev * ctx)
- Line: 192

### xgene_slimpro_i2c_func
- Return type: static u32
- Signature: xgene_slimpro_i2c_func(struct i2c_adapter * adapter)
- Line: 422

### xgene_slimpro_i2c_probe
- Return type: static int
- Signature: xgene_slimpro_i2c_probe(struct platform_device * pdev)
- Line: 436

### xgene_slimpro_i2c_remove
- Return type: static void
- Signature: xgene_slimpro_i2c_remove(struct platform_device * pdev)
- Line: 522

### xgene_slimpro_i2c_xfer
- Return type: static int
- Signature: xgene_slimpro_i2c_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 331

### xgene_word_tst_and_clr
- Return type: static u16
- Signature: xgene_word_tst_and_clr(u16 * addr,u16 mask)
- Line: 117

## Structs (1)

### slimpro_i2c_dev
- Line: 94
- Members:
  - adapter: i2c_adapter
  - dev: device *
  - mbox_chan: mbox_chan *
  - pcc_chan: pcc_mbox_chan *
  - mbox_client: mbox_client
  - mbox_idx: int
  - rd_complete: completion
  - dma_buffer: u8[]
  - resp_msg: u32 *

## Enums (1)

### slimpro_i2c_version
- Line: 109

## Variables (4)

- static **xgene_slimpro_i2c_acpi_ids** : const struct acpi_device_id[] (line 541)
- static **xgene_slimpro_i2c_algorithm** : const struct i2c_algorithm (line 431)
- static **xgene_slimpro_i2c_driver** : platform_driver (line 549)
- static **xgene_slimpro_i2c_dt_ids** : const struct of_device_id[] (line 534)

## Macros (38)

- **BLOCK_DATA** (line 30)
- **BYTE_DATA** (line 28)
- **IIC_SMB_WITHOUT_DATA_LEN** (line 38)
- **IIC_SMB_WITH_DATA_LEN** (line 39)
- **MAILBOX_I2C_INDEX** (line 24)
- **MAILBOX_OP_TIMEOUT** (line 23)
- **SLIMPRO_DBGMSG_TYPE_MASK** (line 45)
- **SLIMPRO_DBGMSG_TYPE_SHIFT** (line 44)
- **SLIMPRO_DBG_SUBTYPE_I2C1READ** (line 43)
- **SLIMPRO_DEBUG_MSG** (line 41)
- **SLIMPRO_IIC_ADDRLEN_MASK** (line 55)
- **SLIMPRO_IIC_ADDRLEN_SHIFT** (line 54)
- **SLIMPRO_IIC_BUS** (line 25)
- **SLIMPRO_IIC_DATALEN_MASK** (line 57)
- **SLIMPRO_IIC_DATALEN_SHIFT** (line 56)
- **SLIMPRO_IIC_DEVID_MASK** (line 49)
- **SLIMPRO_IIC_DEVID_SHIFT** (line 48)
- **SLIMPRO_IIC_DEV_MASK** (line 47)
- **SLIMPRO_IIC_DEV_SHIFT** (line 46)
- **SLIMPRO_IIC_ENCODE_ADDR**(a) (line 90)
- **SLIMPRO_IIC_ENCODE_FLAG_BUFADDR** (line 85)
- **SLIMPRO_IIC_ENCODE_FLAG_WITH_DATA_LEN**(a) (line 86)
- **SLIMPRO_IIC_ENCODE_MSG**(dev,chip,op,proto,addrlen,datalen) (line 69)
- **SLIMPRO_IIC_ENCODE_UPPER_BUFADDR**(a) (line 88)
- **SLIMPRO_IIC_I2C_PROTOCOL** (line 32)
- **SLIMPRO_IIC_MSG_DWORD_COUNT** (line 92)
- **SLIMPRO_IIC_PROTO_MASK** (line 53)
- **SLIMPRO_IIC_PROTO_SHIFT** (line 52)
- **SLIMPRO_IIC_READ** (line 35)
- **SLIMPRO_IIC_RW_MASK** (line 51)
- **SLIMPRO_IIC_RW_SHIFT** (line 50)
- **SLIMPRO_IIC_SMB_PROTOCOL** (line 33)
- **SLIMPRO_IIC_WRITE** (line 36)
- **SLIMPRO_MSG_TYPE**(v) (line 80)
- **SLIMPRO_MSG_TYPE_SHIFT** (line 42)
- **SMBUS_CMD_LEN** (line 27)
- **WORD_DATA** (line 29)
- **to_slimpro_i2c_dev**(cl) (line 106)
