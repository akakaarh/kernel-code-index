# drivers/mmc/core/sdio_uart.c

Subsystem: drivers/mmc

## Functions (44)

### sdio_in
- Return type: static u8
- Signature: sdio_in(struct sdio_uart_port * port,int offset)
- Line: 181

### sdio_out
- Return type: static void
- Signature: sdio_out(struct sdio_uart_port * port,int offset,int value)
- Line: 186

### sdio_uart_activate
- Return type: static int
- Signature: sdio_uart_activate(struct tty_port * tport,struct tty_struct * tty)
- Line: 576

### sdio_uart_add_port
- Return type: static int
- Signature: sdio_uart_add_port(struct sdio_uart_port * port)
- Line: 87

### sdio_uart_break_ctl
- Return type: static int
- Signature: sdio_uart_break_ctl(struct tty_struct * tty,int break_state)
- Line: 896

### sdio_uart_change_speed
- Return type: static void
- Signature: sdio_uart_change_speed(struct sdio_uart_port * port,struct ktermios * termios,const struct ktermios * old)
- Line: 245

### sdio_uart_chars_in_buffer
- Return type: static unsigned int
- Signature: sdio_uart_chars_in_buffer(struct tty_struct * tty)
- Line: 788

### sdio_uart_check_modem_status
- Return type: static void
- Signature: sdio_uart_check_modem_status(struct sdio_uart_port * port)
- Line: 446

### sdio_uart_claim_func
- Return type: static int
- Signature: sdio_uart_claim_func(struct sdio_uart_port * port)
- Line: 162

### sdio_uart_cleanup
- Return type: static void
- Signature: sdio_uart_cleanup(struct tty_struct * tty)
- Line: 730

### sdio_uart_close
- Return type: static void
- Signature: sdio_uart_close(struct tty_struct * tty,struct file * filp)
- Line: 747

### sdio_uart_exit
- Return type: static void __exit
- Signature: sdio_uart_exit(void)
- Line: 1154

### sdio_uart_get_mctrl
- Return type: static unsigned int
- Signature: sdio_uart_get_mctrl(struct sdio_uart_port * port)
- Line: 191

### sdio_uart_hangup
- Return type: static void
- Signature: sdio_uart_hangup(struct tty_struct * tty)
- Line: 753

### sdio_uart_init
- Return type: static int __init
- Signature: sdio_uart_init(void)
- Line: 1115

### sdio_uart_install
- Return type: static int
- Signature: sdio_uart_install(struct tty_driver * driver,struct tty_struct * tty)
- Line: 708

### sdio_uart_irq
- Return type: static void
- Signature: sdio_uart_irq(struct sdio_func * func)
- Line: 495

### sdio_uart_open
- Return type: static int
- Signature: sdio_uart_open(struct tty_struct * tty,struct file * filp)
- Line: 741

### sdio_uart_port_destroy
- Return type: static void
- Signature: sdio_uart_port_destroy(struct tty_port * tport)
- Line: 691

### sdio_uart_port_get
- Return type: static sdio_uart_port *
- Signature: sdio_uart_port_get(unsigned index)
- Line: 110

### sdio_uart_port_put
- Return type: static void
- Signature: sdio_uart_port_put(struct sdio_uart_port * port)
- Line: 126

### sdio_uart_port_remove
- Return type: static void
- Signature: sdio_uart_port_remove(struct sdio_uart_port * port)
- Line: 131

### sdio_uart_probe
- Return type: static int
- Signature: sdio_uart_probe(struct sdio_func * func,const struct sdio_device_id * id)
- Line: 1018

### sdio_uart_proc_show
- Return type: static int
- Signature: sdio_uart_proc_show(struct seq_file * m,void * v)
- Line: 944

### sdio_uart_receive_chars
- Return type: static void
- Signature: sdio_uart_receive_chars(struct sdio_uart_port * port,u8 * status)
- Line: 355

### sdio_uart_release_func
- Return type: static void
- Signature: sdio_uart_release_func(struct sdio_uart_port * port)
- Line: 175

### sdio_uart_remove
- Return type: static void
- Signature: sdio_uart_remove(struct sdio_func * func)
- Line: 1092

### sdio_uart_send_xchar
- Return type: static void
- Signature: sdio_uart_send_xchar(struct tty_struct * tty,u8 ch)
- Line: 794

### sdio_uart_set_termios
- Return type: static void
- Signature: sdio_uart_set_termios(struct tty_struct * tty,const struct ktermios * old_termios)
- Line: 856

### sdio_uart_shutdown
- Return type: static void
- Signature: sdio_uart_shutdown(struct tty_port * tport)
- Line: 659

### sdio_uart_start_tx
- Return type: static void
- Signature: sdio_uart_start_tx(struct sdio_uart_port * port)
- Line: 332

### sdio_uart_stop_rx
- Return type: static void
- Signature: sdio_uart_stop_rx(struct sdio_uart_port * port)
- Line: 348

### sdio_uart_stop_tx
- Return type: static void
- Signature: sdio_uart_stop_tx(struct sdio_uart_port * port)
- Line: 340

### sdio_uart_throttle
- Return type: static void
- Signature: sdio_uart_throttle(struct tty_struct * tty)
- Line: 808

### sdio_uart_tiocmget
- Return type: static int
- Signature: sdio_uart_tiocmget(struct tty_struct * tty)
- Line: 915

### sdio_uart_tiocmset
- Return type: static int
- Signature: sdio_uart_tiocmset(struct tty_struct * tty,unsigned int set,unsigned int clear)
- Line: 929

### sdio_uart_transmit_chars
- Return type: static void
- Signature: sdio_uart_transmit_chars(struct sdio_uart_port * port)
- Line: 407

### sdio_uart_unthrottle
- Return type: static void
- Signature: sdio_uart_unthrottle(struct tty_struct * tty)
- Line: 830

### sdio_uart_update_mctrl
- Return type: static void
- Signature: sdio_uart_update_mctrl(struct sdio_uart_port * port,unsigned int set,unsigned int clear)
- Line: 231

### sdio_uart_write
- Return type: static ssize_t
- Signature: sdio_uart_write(struct tty_struct * tty,const u8 * buf,size_t count)
- Line: 759

### sdio_uart_write_mctrl
- Return type: static void
- Signature: sdio_uart_write_mctrl(struct sdio_uart_port * port,unsigned int mctrl)
- Line: 212

### sdio_uart_write_room
- Return type: static unsigned int
- Signature: sdio_uart_write_room(struct tty_struct * tty)
- Line: 782

### uart_carrier_raised
- Return type: static bool
- Signature: uart_carrier_raised(struct tty_port * tport)
- Line: 525

### uart_dtr_rts
- Return type: static void
- Signature: uart_dtr_rts(struct tty_port * tport,bool active)
- Line: 547

## Structs (2)

### sdio_uart_port
- Line: 64
- Members:
  - cts: __u32
  - dsr: __u32
  - rng: __u32
  - dcd: __u32
  - rx: __u32
  - tx: __u32
  - frame: __u32
  - overrun: __u32
  - parity: __u32
  - brk: __u32
  - port: tty_port
  - index: unsigned int
  - func: sdio_func *
  - func_lock: mutex
  - in_sdio_uart_irq: task_struct *
  - regs_offset: unsigned int
  - xmit_fifo: kfifo
  - write_lock: spinlock_t
  - icount: uart_icount
  - uartclk: unsigned int
  - mctrl: unsigned int
  - rx_mctrl: unsigned int
  - read_status_mask: unsigned int
  - ignore_status_mask: unsigned int
  - x_char: unsigned char
  - ier: unsigned char
  - lcr: unsigned char

### uart_icount
- Line: 51
- Members:
  - cts: __u32
  - dsr: __u32
  - rng: __u32
  - dcd: __u32
  - rx: __u32
  - tx: __u32
  - frame: __u32
  - overrun: __u32
  - parity: __u32
  - brk: __u32
  - port: tty_port
  - index: unsigned int
  - func: sdio_func *
  - func_lock: mutex
  - in_sdio_uart_irq: task_struct *
  - regs_offset: unsigned int
  - xmit_fifo: kfifo
  - write_lock: spinlock_t
  - icount: uart_icount
  - uartclk: unsigned int
  - mctrl: unsigned int
  - rx_mctrl: unsigned int
  - read_status_mask: unsigned int
  - ignore_status_mask: unsigned int
  - x_char: unsigned char
  - ier: unsigned char
  - lcr: unsigned char

## Variables (6)

- static **sdio_uart_driver** : sdio_driver (line 1108)
- static **sdio_uart_ids** : const struct sdio_device_id[] (line 1100)
- static **sdio_uart_ops** : const struct tty_operations (line 997)
- static **sdio_uart_port_ops** : const struct tty_port_operations (line 989)
- static **sdio_uart_table** : sdio_uart_port * [] (line 84)
- static **sdio_uart_tty_driver** : tty_driver * (line 1016)

## Macros (5)

- **FIFO_SIZE** (line 48)
- **UART_NR** (line 45)
- **WAKEUP_CHARS** (line 49)
- **sdio_uart_clear_mctrl**(port,x) (line 243)
- **sdio_uart_set_mctrl**(port,x) (line 242)
