# drivers/i2c/busses/i2c-cpm.c

Subsystem: drivers/i2c

## Functions (11)

### cpm_i2c_check_message
- Return type: static int
- Signature: cpm_i2c_check_message(struct i2c_adapter * adap,struct i2c_msg * pmsg,int tx,int rx)
- Line: 240

### cpm_i2c_force_close
- Return type: static void
- Signature: cpm_i2c_force_close(struct i2c_adapter * adap)
- Line: 168

### cpm_i2c_func
- Return type: static u32
- Signature: cpm_i2c_func(struct i2c_adapter * adap)
- Line: 397

### cpm_i2c_interrupt
- Return type: static irqreturn_t
- Signature: cpm_i2c_interrupt(int irq,void * dev_id)
- Line: 117

### cpm_i2c_parse_message
- Return type: static void
- Signature: cpm_i2c_parse_message(struct i2c_adapter * adap,struct i2c_msg * pmsg,int num,int tx,int rx)
- Line: 181

### cpm_i2c_probe
- Return type: static int
- Signature: cpm_i2c_probe(struct platform_device * ofdev)
- Line: 633

### cpm_i2c_remove
- Return type: static void
- Signature: cpm_i2c_remove(struct platform_device * ofdev)
- Line: 679

### cpm_i2c_setup
- Return type: static int
- Signature: cpm_i2c_setup(struct cpm_i2c * cpm)
- Line: 423

### cpm_i2c_shutdown
- Return type: static void
- Signature: cpm_i2c_shutdown(struct cpm_i2c * cpm)
- Line: 603

### cpm_i2c_xfer
- Return type: static int
- Signature: cpm_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 297

### cpm_reset_i2c_params
- Return type: static void
- Signature: cpm_reset_i2c_params(struct cpm_i2c * cpm)
- Line: 138

## Structs (3)

### cpm_i2c
- Line: 96
- Members:
  - rbase: ushort
  - tbase: ushort
  - rfcr: u_char
  - tfcr: u_char
  - mrblr: ushort
  - rstate: uint
  - rdp: uint
  - rbptr: ushort
  - rbc: ushort
  - rxtmp: uint
  - tstate: uint
  - tdp: uint
  - tbptr: ushort
  - tbc: ushort
  - txtmp: uint
  - res1: char[4]
  - rpbase: ushort
  - res2: char[2]
  - res3: char[4]
  - sdmatmp: uint
  - i2mod: u8
  - res1: u8[3]
  - i2add: u8
  - res2: u8[3]
  - i2brg: u8
  - res3: u8[3]
  - i2com: u8
  - res4: u8[3]
  - i2cer: u8
  - res5: u8[3]
  - i2cmr: u8
  - base: char *
  - ofdev: platform_device *
  - adap: i2c_adapter
  - dp_addr: uint
  - version: int
  - irq: int
  - cp_command: int
  - freq: int
  - i2c_reg: i2c_reg __iomem *
  - i2c_ram: i2c_ram __iomem *
  - i2c_addr: u16
  - i2c_wait: wait_queue_head_t
  - tbase: cbd_t __iomem *
  - rbase: cbd_t __iomem *
  - txbuf: u_char * []
  - rxbuf: u_char * []
  - txdma: dma_addr_t[]
  - rxdma: dma_addr_t[]

### i2c_ram
- Line: 49
- Members:
  - rbase: ushort
  - tbase: ushort
  - rfcr: u_char
  - tfcr: u_char
  - mrblr: ushort
  - rstate: uint
  - rdp: uint
  - rbptr: ushort
  - rbc: ushort
  - rxtmp: uint
  - tstate: uint
  - tdp: uint
  - tbptr: ushort
  - tbc: ushort
  - txtmp: uint
  - res1: char[4]
  - rpbase: ushort
  - res2: char[2]
  - res3: char[4]
  - sdmatmp: uint
  - i2mod: u8
  - res1: u8[3]
  - i2add: u8
  - res2: u8[3]
  - i2brg: u8
  - res3: u8[3]
  - i2com: u8
  - res4: u8[3]
  - i2cer: u8
  - res5: u8[3]
  - i2cmr: u8
  - base: char *
  - ofdev: platform_device *
  - adap: i2c_adapter
  - dp_addr: uint
  - version: int
  - irq: int
  - cp_command: int
  - freq: int
  - i2c_reg: i2c_reg __iomem *
  - i2c_ram: i2c_ram __iomem *
  - i2c_addr: u16
  - i2c_wait: wait_queue_head_t
  - tbase: cbd_t __iomem *
  - rbase: cbd_t __iomem *
  - txbuf: u_char * []
  - rxbuf: u_char * []
  - txdma: dma_addr_t[]
  - rxdma: dma_addr_t[]

### i2c_reg
- Line: 82
- Members:
  - rbase: ushort
  - tbase: ushort
  - rfcr: u_char
  - tfcr: u_char
  - mrblr: ushort
  - rstate: uint
  - rdp: uint
  - rbptr: ushort
  - rbc: ushort
  - rxtmp: uint
  - tstate: uint
  - tdp: uint
  - tbptr: ushort
  - tbc: ushort
  - txtmp: uint
  - res1: char[4]
  - rpbase: ushort
  - res2: char[2]
  - res3: char[4]
  - sdmatmp: uint
  - i2mod: u8
  - res1: u8[3]
  - i2add: u8
  - res2: u8[3]
  - i2brg: u8
  - res3: u8[3]
  - i2com: u8
  - res4: u8[3]
  - i2cer: u8
  - res5: u8[3]
  - i2cmr: u8
  - base: char *
  - ofdev: platform_device *
  - adap: i2c_adapter
  - dp_addr: uint
  - version: int
  - irq: int
  - cp_command: int
  - freq: int
  - i2c_reg: i2c_reg __iomem *
  - i2c_ram: i2c_ram __iomem *
  - i2c_addr: u16
  - i2c_wait: wait_queue_head_t
  - tbase: cbd_t __iomem *
  - rbase: cbd_t __iomem *
  - txbuf: u_char * []
  - rxbuf: u_char * []
  - txdma: dma_addr_t[]
  - rxdma: dma_addr_t[]

## Variables (5)

- static **cpm_i2c_algo** : const struct i2c_algorithm (line 404)
- static **cpm_i2c_driver** : platform_driver (line 702)
- static **cpm_i2c_match** : const struct of_device_id[] (line 690)
- static **cpm_i2c_quirks** : const struct i2c_adapter_quirks (line 410)
- static **cpm_ops** : const struct i2c_adapter (line 416)

## Macros (12)

- **CPM_MAXBD** (line 41)
- **CPM_MAX_READ** (line 40)
- **DPRAM_BASE** (line 46)
- **I2CER_BUSY** (line 76)
- **I2CER_RXB** (line 78)
- **I2CER_TXB** (line 77)
- **I2CER_TXE** (line 75)
- **I2COM_MASTER** (line 74)
- **I2COM_START** (line 73)
- **I2C_EB** (line 43)
- **I2C_EB_CPM2** (line 44)
- **I2MOD_EN** (line 79)
