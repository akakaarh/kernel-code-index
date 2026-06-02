# drivers/i2c/busses/scx200_acb.c

Subsystem: drivers/i2c

## Functions (15)

### scx200_acb_cleanup
- Return type: static void __exit
- Signature: scx200_acb_cleanup(void)
- Line: 577

### scx200_acb_create
- Return type: static int
- Signature: scx200_acb_create(struct scx200_acb_iface * iface)
- Line: 438

### scx200_acb_func
- Return type: static u32
- Signature: scx200_acb_func(struct i2c_adapter * adapter)
- Line: 364

### scx200_acb_init
- Return type: static int __init
- Signature: scx200_acb_init(void)
- Line: 562

### scx200_acb_machine
- Return type: static void
- Signature: scx200_acb_machine(struct scx200_acb_iface * iface,u8 status)
- Line: 101

### scx200_acb_poll
- Return type: static void
- Signature: scx200_acb_poll(struct scx200_acb_iface * iface)
- Line: 217

### scx200_acb_probe
- Return type: static int
- Signature: scx200_acb_probe(struct scx200_acb_iface * iface)
- Line: 380

### scx200_acb_reset
- Return type: static void
- Signature: scx200_acb_reset(struct scx200_acb_iface * iface)
- Line: 247

### scx200_acb_smbus_xfer
- Return type: static s32
- Signature: scx200_acb_smbus_xfer(struct i2c_adapter * adapter,u16 address,unsigned short flags,char rw,u8 command,int size,union i2c_smbus_data * data)
- Line: 268

### scx200_cleanup_iface
- Return type: static void
- Signature: scx200_cleanup_iface(struct scx200_acb_iface * iface)
- Line: 517

### scx200_create_dev
- Return type: static scx200_acb_iface *
- Signature: scx200_create_dev(const char * text,unsigned long base,int index,struct device * dev)
- Line: 469

### scx200_create_iface
- Return type: static scx200_acb_iface *
- Signature: scx200_create_iface(const char * text,struct device * dev,int index)
- Line: 415

### scx200_probe
- Return type: static int
- Signature: scx200_probe(struct platform_device * pdev)
- Line: 497

### scx200_remove
- Return type: static void
- Signature: scx200_remove(struct platform_device * pdev)
- Line: 524

### scx200_scan_isa
- Return type: static __init void
- Signature: scx200_scan_isa(void)
- Line: 546

## Structs (1)

### scx200_acb_iface
- Line: 63
- Members:
  - next: scx200_acb_iface *
  - adapter: i2c_adapter
  - base: unsigned
  - mutex: mutex
  - state: scx200_acb_state
  - result: int
  - address_byte: u8
  - command: u8
  - ptr: u8 *
  - needs_reset: char
  - len: unsigned

## Enums (1)

### scx200_acb_state
- Line: 42

## Variables (6)

- static **base** : int[] (line 36)
- static **scx200_acb_algorithm** : const struct i2c_algorithm (line 372)
- static **scx200_acb_list** : scx200_acb_iface * (line 377)
- static **scx200_acb_state_name** : const char * [] (line 52)
- static **scx200_isa** : const struct pci_device_id[] (line 540)
- static **scx200_pci_driver** : platform_driver (line 532)

## Macros (21)

- **ACBADDR** (line 95)
- **ACBCST** (line 87)
- **ACBCST_BB** (line 88)
- **ACBCTL1** (line 89)
- **ACBCTL1_ACK** (line 92)
- **ACBCTL1_NMINTE** (line 91)
- **ACBCTL1_START** (line 94)
- **ACBCTL1_STASTRE** (line 90)
- **ACBCTL1_STOP** (line 93)
- **ACBCTL2** (line 96)
- **ACBCTL2_ENABLE** (line 97)
- **ACBSDA** (line 80)
- **ACBST** (line 81)
- **ACBST_BER** (line 83)
- **ACBST_MASTER** (line 86)
- **ACBST_NEGACK** (line 84)
- **ACBST_SDAST** (line 82)
- **ACBST_STASTR** (line 85)
- **MAX_DEVICES** (line 35)
- **POLL_TIMEOUT** (line 40)
- **pr_fmt**(fmt) (line 14)
