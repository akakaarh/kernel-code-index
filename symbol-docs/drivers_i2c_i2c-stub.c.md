# drivers/i2c/i2c-stub.c

Subsystem: drivers/i2c

## Functions (8)

### i2c_stub_allocate_banks
- Return type: static int __init
- Signature: i2c_stub_allocate_banks(int i)
- Line: 321

### i2c_stub_exit
- Return type: static void __exit
- Signature: i2c_stub_exit(void)
- Line: 406

### i2c_stub_free
- Return type: static void
- Signature: i2c_stub_free(void)
- Line: 350

### i2c_stub_init
- Return type: static int __init
- Signature: i2c_stub_init(void)
- Line: 359

### stub_find_block
- Return type: static smbus_block_data *
- Signature: stub_find_block(struct device * dev,struct stub_chip * chip,u8 command,bool create)
- Line: 89

### stub_func
- Return type: static u32
- Signature: stub_func(struct i2c_adapter * adapter)
- Line: 304

### stub_get_wordp
- Return type: static u16 *
- Signature: stub_get_wordp(struct stub_chip * chip,u8 offset)
- Line: 111

### stub_xfer
- Return type: static s32
- Signature: stub_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 123

## Structs (2)

### smbus_block_data
- Line: 62
- Members:
  - node: list_head
  - command: u8
  - len: u8
  - block: u8[]
  - pointer: u8
  - words: u16[256]
  - smbus_blocks: list_head
  - bank_reg: u8
  - bank_shift: u8
  - bank_mask: u8
  - bank_sel: u8
  - bank_start: u8
  - bank_end: u8
  - bank_size: u16
  - bank_words: u16 *

### stub_chip
- Line: 69
- Members:
  - node: list_head
  - command: u8
  - len: u8
  - block: u8[]
  - pointer: u8
  - words: u16[256]
  - smbus_blocks: list_head
  - bank_reg: u8
  - bank_shift: u8
  - bank_mask: u8
  - bank_sel: u8
  - bank_start: u8
  - bank_end: u8
  - bank_size: u16
  - bank_words: u16 *

## Variables (10)

- static **bank_end** : u8[] (line 58)
- static **bank_mask** : u8[] (line 50)
- static **bank_reg** : u8[] (line 46)
- static **bank_start** : u8[] (line 54)
- static **chip_addr** : unsigned short[] (line 35)
- static **functionality** : unsigned long (line 40)
- static **smbus_algorithm** : const struct i2c_algorithm (line 309)
- static **stub_adapter** : i2c_adapter (line 314)
- static **stub_chips** : stub_chip * (line 86)
- static **stub_chips_nr** : int (line 87)

## Macros (4)

- **MAX_CHIPS** (line 20)
- **STUB_FUNC_ALL** (line 32)
- **STUB_FUNC_DEFAULT** (line 27)
- **pr_fmt**(fmt) (line 10)
