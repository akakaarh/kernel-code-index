# drivers/i2c/i2c-mux.c

Subsystem: drivers/i2c

## Functions (15)

### __i2c_mux_master_xfer
- Return type: static int
- Signature: __i2c_mux_master_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 39

### __i2c_mux_smbus_xfer
- Return type: static int
- Signature: __i2c_mux_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 77

### i2c_mux_add_adapter
- Return type: int
- Signature: i2c_mux_add_adapter(struct i2c_mux_core * muxc,u32 force_nr,u32 chan_id)
- Line: 267

### i2c_mux_alloc
- Return type: i2c_mux_core *
- Signature: i2c_mux_alloc(struct i2c_adapter * parent,struct device * dev,int max_adapters,int sizeof_priv,u32 flags,int (* select)(struct i2c_mux_core *,u32),int (* deselect)(struct i2c_mux_core *,u32))
- Line: 226

### i2c_mux_del_adapters
- Return type: void
- Signature: i2c_mux_del_adapters(struct i2c_mux_core * muxc)
- Line: 416

### i2c_mux_functionality
- Return type: static u32
- Signature: i2c_mux_functionality(struct i2c_adapter * adap)
- Line: 122

### i2c_mux_lock_bus
- Return type: static void
- Signature: i2c_mux_lock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 130

### i2c_mux_master_xfer
- Return type: static int
- Signature: i2c_mux_master_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 58

### i2c_mux_smbus_xfer
- Return type: static int
- Signature: i2c_mux_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 99

### i2c_mux_trylock_bus
- Return type: static int
- Signature: i2c_mux_trylock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 141

### i2c_mux_unlock_bus
- Return type: static void
- Signature: i2c_mux_unlock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 156

### i2c_parent_lock_bus
- Return type: static void
- Signature: i2c_parent_lock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 166

### i2c_parent_trylock_bus
- Return type: static int
- Signature: i2c_parent_trylock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 176

### i2c_parent_unlock_bus
- Return type: static void
- Signature: i2c_parent_unlock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 190

### i2c_root_adapter
- Return type: i2c_adapter *
- Signature: i2c_root_adapter(struct device * dev)
- Line: 200

## Structs (1)

### i2c_mux_priv
- Line: 32
- Members:
  - adap: i2c_adapter
  - algo: i2c_algorithm
  - muxc: i2c_mux_core *
  - chan_id: u32

## Variables (2)

- static **i2c_mux_lock_ops** : const struct i2c_lock_operations (line 255)
- static **i2c_parent_lock_ops** : const struct i2c_lock_operations (line 261)
