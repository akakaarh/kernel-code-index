# drivers/i2c/i2c-atr.c

Subsystem: drivers/i2c

## Functions (28)

### i2c_atr_add_adapter
- Return type: int
- Signature: i2c_atr_add_adapter(struct i2c_atr * atr,struct i2c_atr_adap_desc * desc)
- Line: 774

### i2c_atr_alloc_alias_pool
- Return type: static i2c_atr_alias_pool *
- Signature: i2c_atr_alloc_alias_pool(size_t num_aliases,bool shared)
- Line: 135

### i2c_atr_attach_addr
- Return type: static int
- Signature: i2c_atr_attach_addr(struct i2c_adapter * adapter,u16 addr)
- Line: 535

### i2c_atr_bus_notifier_call
- Return type: static int
- Signature: i2c_atr_bus_notifier_call(struct notifier_block * nb,unsigned long event,void * device)
- Line: 591

### i2c_atr_create_c2a
- Return type: static i2c_atr_alias_pair *
- Signature: i2c_atr_create_c2a(struct i2c_atr_chan * chan,u16 alias,u16 addr)
- Line: 170

### i2c_atr_create_mapping_by_addr
- Return type: static i2c_atr_alias_pair *
- Signature: i2c_atr_create_mapping_by_addr(struct i2c_atr_chan * chan,u16 addr)
- Line: 251

### i2c_atr_del_adapter
- Return type: void
- Signature: i2c_atr_del_adapter(struct i2c_atr * atr,u32 chan_id)
- Line: 891

### i2c_atr_delete
- Return type: void
- Signature: i2c_atr_delete(struct i2c_atr * atr)
- Line: 759

### i2c_atr_destroy_c2a
- Return type: static void
- Signature: i2c_atr_destroy_c2a(struct i2c_atr_alias_pair ** pc2a)
- Line: 190

### i2c_atr_detach_addr
- Return type: static void
- Signature: i2c_atr_detach_addr(struct i2c_adapter * adapter,u16 addr)
- Line: 563

### i2c_atr_find_mapping_by_addr
- Return type: static i2c_atr_alias_pair *
- Signature: i2c_atr_find_mapping_by_addr(struct i2c_atr_chan * chan,u16 addr)
- Line: 236

### i2c_atr_free_alias_pool
- Return type: static void
- Signature: i2c_atr_free_alias_pool(struct i2c_atr_alias_pool * alias_pool)
- Line: 163

### i2c_atr_functionality
- Return type: static u32
- Signature: i2c_atr_functionality(struct i2c_adapter * adap)
- Line: 497

### i2c_atr_get_driver_data
- Return type: void *
- Signature: i2c_atr_get_driver_data(struct i2c_atr * atr)
- Line: 936

### i2c_atr_get_mapping_by_addr
- Return type: static i2c_atr_alias_pair *
- Signature: i2c_atr_get_mapping_by_addr(struct i2c_atr_chan * chan,u16 addr)
- Line: 333

### i2c_atr_lock_bus
- Return type: static void
- Signature: i2c_atr_lock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 505

### i2c_atr_map_msgs
- Return type: static int
- Signature: i2c_atr_map_msgs(struct i2c_atr_chan * chan,struct i2c_msg * msgs,int num)
- Line: 359

### i2c_atr_master_xfer
- Return type: static int
- Signature: i2c_atr_master_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 442

### i2c_atr_new
- Return type: i2c_atr *
- Signature: i2c_atr_new(struct i2c_adapter * parent,struct device * dev,const struct i2c_atr_ops * ops,int max_adapters,u32 flags)
- Line: 705

### i2c_atr_parse_alias_pool
- Return type: static int
- Signature: i2c_atr_parse_alias_pool(struct i2c_atr * atr)
- Line: 633

### i2c_atr_release_alias
- Return type: static void
- Signature: i2c_atr_release_alias(struct i2c_atr_alias_pool * alias_pool,u16 alias)
- Line: 218

### i2c_atr_replace_mapping_by_addr
- Return type: static i2c_atr_alias_pair *
- Signature: i2c_atr_replace_mapping_by_addr(struct i2c_atr_chan * chan,u16 addr)
- Line: 287

### i2c_atr_reserve_alias
- Return type: static int
- Signature: i2c_atr_reserve_alias(struct i2c_atr_alias_pool * alias_pool)
- Line: 197

### i2c_atr_set_driver_data
- Return type: void
- Signature: i2c_atr_set_driver_data(struct i2c_atr * atr,void * data)
- Line: 930

### i2c_atr_smbus_xfer
- Return type: static int
- Signature: i2c_atr_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 469

### i2c_atr_trylock_bus
- Return type: static int
- Signature: i2c_atr_trylock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 513

### i2c_atr_unlock_bus
- Return type: static void
- Signature: i2c_atr_unlock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 521

### i2c_atr_unmap_msgs
- Return type: static void
- Signature: i2c_atr_unmap_msgs(struct i2c_atr_chan * chan,struct i2c_msg * msgs,int num)
- Line: 419

## Structs (4)

### i2c_atr
- Line: 114
- Members:
  - node: list_head
  - fixed: bool
  - addr: u16
  - alias: u16
  - size: size_t
  - shared: bool
  - lock: spinlock_t
  - use_mask: unsigned long *
  - adap: i2c_adapter
  - atr: i2c_atr *
  - chan_id: u32
  - alias_pairs_lock: mutex
  - alias_pairs_lock_key: lock_class_key
  - alias_pairs: list_head
  - alias_pool: i2c_atr_alias_pool *
  - orig_addrs_lock: mutex
  - orig_addrs_lock_key: lock_class_key
  - orig_addrs: u16 *
  - orig_addrs_size: unsigned int
  - parent: i2c_adapter *
  - dev: device *
  - ops: const struct i2c_atr_ops *
  - priv: void *
  - algo: i2c_algorithm
  - lock: mutex
  - lock_key: lock_class_key
  - max_adapters: int
  - flags: u32
  - alias_pool: i2c_atr_alias_pool *
  - i2c_nb: notifier_block

### i2c_atr_alias_pair
- Line: 39
- Members:
  - node: list_head
  - fixed: bool
  - addr: u16
  - alias: u16
  - size: size_t
  - shared: bool
  - lock: spinlock_t
  - use_mask: unsigned long *
  - adap: i2c_adapter
  - atr: i2c_atr *
  - chan_id: u32
  - alias_pairs_lock: mutex
  - alias_pairs_lock_key: lock_class_key
  - alias_pairs: list_head
  - alias_pool: i2c_atr_alias_pool *
  - orig_addrs_lock: mutex
  - orig_addrs_lock_key: lock_class_key
  - orig_addrs: u16 *
  - orig_addrs_size: unsigned int
  - parent: i2c_adapter *
  - dev: device *
  - ops: const struct i2c_atr_ops *
  - priv: void *
  - algo: i2c_algorithm
  - lock: mutex
  - lock_key: lock_class_key
  - max_adapters: int
  - flags: u32
  - alias_pool: i2c_atr_alias_pool *
  - i2c_nb: notifier_block

### i2c_atr_alias_pool
- Line: 55
- Members:
  - node: list_head
  - fixed: bool
  - addr: u16
  - alias: u16
  - size: size_t
  - shared: bool
  - lock: spinlock_t
  - use_mask: unsigned long *
  - adap: i2c_adapter
  - atr: i2c_atr *
  - chan_id: u32
  - alias_pairs_lock: mutex
  - alias_pairs_lock_key: lock_class_key
  - alias_pairs: list_head
  - alias_pool: i2c_atr_alias_pool *
  - orig_addrs_lock: mutex
  - orig_addrs_lock_key: lock_class_key
  - orig_addrs: u16 *
  - orig_addrs_size: unsigned int
  - parent: i2c_adapter *
  - dev: device *
  - ops: const struct i2c_atr_ops *
  - priv: void *
  - algo: i2c_algorithm
  - lock: mutex
  - lock_key: lock_class_key
  - max_adapters: int
  - flags: u32
  - alias_pool: i2c_atr_alias_pool *
  - i2c_nb: notifier_block

### i2c_atr_chan
- Line: 81
- Members:
  - node: list_head
  - fixed: bool
  - addr: u16
  - alias: u16
  - size: size_t
  - shared: bool
  - lock: spinlock_t
  - use_mask: unsigned long *
  - adap: i2c_adapter
  - atr: i2c_atr *
  - chan_id: u32
  - alias_pairs_lock: mutex
  - alias_pairs_lock_key: lock_class_key
  - alias_pairs: list_head
  - alias_pool: i2c_atr_alias_pool *
  - orig_addrs_lock: mutex
  - orig_addrs_lock_key: lock_class_key
  - orig_addrs: u16 *
  - orig_addrs_size: unsigned int
  - parent: i2c_adapter *
  - dev: device *
  - ops: const struct i2c_atr_ops *
  - priv: void *
  - algo: i2c_algorithm
  - lock: mutex
  - lock_key: lock_class_key
  - max_adapters: int
  - flags: u32
  - alias_pool: i2c_atr_alias_pool *
  - i2c_nb: notifier_block

## Variables (1)

- static **i2c_atr_lock_ops** : const struct i2c_lock_operations (line 529)

## Macros (2)

- **ATR_MAX_ADAPTERS** (line 21)
- **ATR_MAX_SYMLINK_LEN** (line 22)
