# drivers/i2c/busses/i2c-iop3xx.c

Subsystem: drivers/i2c

## Functions (23)

### all_bits_clear
- Return type: static int
- Signature: all_bits_clear(unsigned test,unsigned mask)
- Line: 193

### any_bits_set
- Return type: static int
- Signature: any_bits_set(unsigned test,unsigned mask)
- Line: 199

### iic_cook_addr
- Return type: static unsigned char
- Signature: iic_cook_addr(struct i2c_msg * msg)
- Line: 46

### iop3xx_i2c_enable
- Return type: static void
- Signature: iop3xx_i2c_enable(struct i2c_algo_iop3xx_data * iop3xx_adap)
- Line: 65

### iop3xx_i2c_error
- Return type: static int
- Signature: iop3xx_i2c_error(u32 sr)
- Line: 123

### iop3xx_i2c_func
- Return type: static u32
- Signature: iop3xx_i2c_func(struct i2c_adapter * adap)
- Line: 378

### iop3xx_i2c_get_srstat
- Return type: static u32
- Signature: iop3xx_i2c_get_srstat(struct i2c_algo_iop3xx_data * iop3xx_adap)
- Line: 139

### iop3xx_i2c_handle_msg
- Return type: static int
- Signature: iop3xx_i2c_handle_msg(struct i2c_adapter * i2c_adap,struct i2c_msg * pmsg)
- Line: 335

### iop3xx_i2c_irq_handler
- Return type: static irqreturn_t
- Signature: iop3xx_i2c_irq_handler(int this_irq,void * dev_id)
- Line: 108

### iop3xx_i2c_probe
- Return type: static int
- Signature: iop3xx_i2c_probe(struct platform_device * pdev)
- Line: 411

### iop3xx_i2c_read_byte
- Return type: static int
- Signature: iop3xx_i2c_read_byte(struct i2c_algo_iop3xx_data * iop3xx_adap,char * byte,int stop)
- Line: 278

### iop3xx_i2c_readbytes
- Return type: static int
- Signature: iop3xx_i2c_readbytes(struct i2c_adapter * i2c_adap,char * buf,int count)
- Line: 315

### iop3xx_i2c_remove
- Return type: static void
- Signature: iop3xx_i2c_remove(struct platform_device * pdev)
- Line: 389

### iop3xx_i2c_reset
- Return type: static void
- Signature: iop3xx_i2c_reset(struct i2c_algo_iop3xx_data * iop3xx_adap)
- Line: 56

### iop3xx_i2c_send_target_addr
- Return type: static int
- Signature: iop3xx_i2c_send_target_addr(struct i2c_algo_iop3xx_data * iop3xx_adap,struct i2c_msg * msg)
- Line: 230

### iop3xx_i2c_transaction_cleanup
- Return type: static void
- Signature: iop3xx_i2c_transaction_cleanup(struct i2c_algo_iop3xx_data * iop3xx_adap)
- Line: 93

### iop3xx_i2c_wait_event
- Return type: static int
- Signature: iop3xx_i2c_wait_event(struct i2c_algo_iop3xx_data * iop3xx_adap,unsigned flags,unsigned * status,compare_func compare)
- Line: 160

### iop3xx_i2c_wait_idle
- Return type: static int
- Signature: iop3xx_i2c_wait_idle(struct i2c_algo_iop3xx_data * iop3xx_adap,int * status)
- Line: 223

### iop3xx_i2c_wait_rx_done
- Return type: static int
- Signature: iop3xx_i2c_wait_rx_done(struct i2c_algo_iop3xx_data * iop3xx_adap,int * status)
- Line: 214

### iop3xx_i2c_wait_tx_done
- Return type: static int
- Signature: iop3xx_i2c_wait_tx_done(struct i2c_algo_iop3xx_data * iop3xx_adap,int * status)
- Line: 205

### iop3xx_i2c_write_byte
- Return type: static int
- Signature: iop3xx_i2c_write_byte(struct i2c_algo_iop3xx_data * iop3xx_adap,char byte,int stop)
- Line: 256

### iop3xx_i2c_writebytes
- Return type: static int
- Signature: iop3xx_i2c_writebytes(struct i2c_adapter * i2c_adap,const char * buf,int count)
- Line: 303

### iop3xx_i2c_xfer
- Return type: static int
- Signature: iop3xx_i2c_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg * msgs,int num)
- Line: 353

## Typedefs (1)

- **compare_func** → int (*)(unsigned test,unsigned mask) (line 156)

## Variables (4)

- static **i2c_id** : int (line 43)
- static **i2c_iop3xx_match** : const struct of_device_id[] (line 518)
- static **iop3xx_i2c_algo** : const struct i2c_algorithm (line 383)
- static **iop3xx_i2c_driver** : platform_driver (line 525)
