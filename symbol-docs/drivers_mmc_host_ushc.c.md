# drivers/mmc/host/ushc.c

Subsystem: drivers/mmc

## Functions (17)

### cbw_callback
- Return type: static void
- Signature: cbw_callback(struct urb * urb)
- Line: 197

### csw_callback
- Return type: static void
- Signature: csw_callback(struct urb * urb)
- Line: 215

### data_callback
- Return type: static void
- Signature: data_callback(struct urb * urb)
- Line: 207

### int_callback
- Return type: static void
- Signature: int_callback(struct urb * urb)
- Line: 163

### ushc_clean_up
- Return type: static void
- Signature: ushc_clean_up(struct ushc_data * ushc)
- Line: 397

### ushc_disconnect
- Return type: static void
- Signature: ushc_disconnect(struct usb_interface * intf)
- Line: 530

### ushc_enable_sdio_irq
- Return type: static void
- Signature: ushc_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 387

### ushc_get_cd
- Return type: static int
- Signature: ushc_get_cd(struct mmc_host * mmc)
- Line: 380

### ushc_hw_get_caps
- Return type: static int
- Signature: ushc_hw_get_caps(struct ushc_data * ushc)
- Line: 126

### ushc_hw_reset
- Return type: static int
- Signature: ushc_hw_reset(struct ushc_data * ushc)
- Line: 119

### ushc_hw_set_host_ctrl
- Return type: static int
- Signature: ushc_hw_set_host_ctrl(struct ushc_data * ushc,u16 mask,u16 val)
- Line: 148

### ushc_probe
- Return type: static int
- Signature: ushc_probe(struct usb_interface * intf,const struct usb_device_id * id)
- Line: 416

### ushc_request
- Return type: static void
- Signature: ushc_request(struct mmc_host * mmc,struct mmc_request * req)
- Line: 248

### ushc_set_bus_freq
- Return type: static int
- Signature: ushc_set_bus_freq(struct ushc_data * ushc,int clk,bool enable_hs)
- Line: 348

### ushc_set_bus_width
- Return type: static int
- Signature: ushc_set_bus_width(struct ushc_data * ushc,int bus_width)
- Line: 342

### ushc_set_ios
- Return type: static void
- Signature: ushc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 371

### ushc_set_power
- Return type: static int
- Signature: ushc_set_power(struct ushc_data * ushc,unsigned char power_mode)
- Line: 321

## Structs (4)

### ushc_cbw
- Line: 63
- Members:
  - signature: __u8
  - cmd_idx: __u8
  - block_size: __le16
  - arg: __le32
  - signature: __u8
  - status: __u8
  - response: __le32
  - status: u8
  - reserved: u8[3]
  - usb_dev: usb_device *
  - mmc: mmc_host *
  - int_urb: urb *
  - int_data: ushc_int_data *
  - cbw_urb: urb *
  - cbw: ushc_cbw *
  - data_urb: urb *
  - csw_urb: urb *
  - csw: ushc_csw *
  - lock: spinlock_t
  - current_req: mmc_request *
  - caps: u32
  - host_ctrl: u16
  - flags: unsigned long
  - last_status: u8
  - clock_freq: int

### ushc_csw
- Line: 72
- Members:
  - signature: __u8
  - cmd_idx: __u8
  - block_size: __le16
  - arg: __le32
  - signature: __u8
  - status: __u8
  - response: __le32
  - status: u8
  - reserved: u8[3]
  - usb_dev: usb_device *
  - mmc: mmc_host *
  - int_urb: urb *
  - int_data: ushc_int_data *
  - cbw_urb: urb *
  - cbw: ushc_cbw *
  - data_urb: urb *
  - csw_urb: urb *
  - csw: ushc_csw *
  - lock: spinlock_t
  - current_req: mmc_request *
  - caps: u32
  - host_ctrl: u16
  - flags: unsigned long
  - last_status: u8
  - clock_freq: int

### ushc_data
- Line: 89
- Members:
  - signature: __u8
  - cmd_idx: __u8
  - block_size: __le16
  - arg: __le32
  - signature: __u8
  - status: __u8
  - response: __le32
  - status: u8
  - reserved: u8[3]
  - usb_dev: usb_device *
  - mmc: mmc_host *
  - int_urb: urb *
  - int_data: ushc_int_data *
  - cbw_urb: urb *
  - cbw: ushc_cbw *
  - data_urb: urb *
  - csw_urb: urb *
  - csw: ushc_csw *
  - lock: spinlock_t
  - current_req: mmc_request *
  - caps: u32
  - host_ctrl: u16
  - flags: unsigned long
  - last_status: u8
  - clock_freq: int

### ushc_int_data
- Line: 80
- Members:
  - signature: __u8
  - cmd_idx: __u8
  - block_size: __le16
  - arg: __le32
  - signature: __u8
  - status: __u8
  - response: __le32
  - status: u8
  - reserved: u8[3]
  - usb_dev: usb_device *
  - mmc: mmc_host *
  - int_urb: urb *
  - int_data: ushc_int_data *
  - cbw_urb: urb *
  - cbw: ushc_cbw *
  - data_urb: urb *
  - csw_urb: urb *
  - csw: ushc_csw *
  - lock: spinlock_t
  - current_req: mmc_request *
  - caps: u32
  - host_ctrl: u16
  - flags: unsigned long
  - last_status: u8
  - clock_freq: int

## Enums (2)

### ushc_request
- Line: 22

### ushc_request_type
- Line: 32

## Variables (3)

- static **ushc_driver** : usb_driver (line 555)
- static **ushc_id_table** : usb_device_id[] (line 548)
- static **ushc_ops** : const struct mmc_host_ops (line 409)

## Macros (24)

- **DISCONNECTED** (line 113)
- **IGNORE_NEXT_INT** (line 115)
- **INT_EN** (line 114)
- **USHC_CBW_SIGNATURE** (line 70)
- **USHC_CSW_SIGNATURE** (line 78)
- **USHC_GET_CAPS_1V8** (line 45)
- **USHC_GET_CAPS_3V0** (line 44)
- **USHC_GET_CAPS_3V3** (line 43)
- **USHC_GET_CAPS_HIGH_SPD** (line 46)
- **USHC_GET_CAPS_VERSION_MASK** (line 42)
- **USHC_HOST_CTRL_4BIT** (line 48)
- **USHC_HOST_CTRL_HIGH_SPD** (line 49)
- **USHC_INT_STATUS_CARD_PRESENT** (line 86)
- **USHC_INT_STATUS_SDIO_INT** (line 85)
- **USHC_PWR_CTRL_1V8** (line 54)
- **USHC_PWR_CTRL_3V0** (line 53)
- **USHC_PWR_CTRL_3V3** (line 52)
- **USHC_PWR_CTRL_OFF** (line 51)
- **USHC_READ_RESP_BUSY** (line 56)
- **USHC_READ_RESP_ERR_CMD** (line 60)
- **USHC_READ_RESP_ERR_CRC** (line 58)
- **USHC_READ_RESP_ERR_DAT** (line 59)
- **USHC_READ_RESP_ERR_MASK** (line 61)
- **USHC_READ_RESP_ERR_TIMEOUT** (line 57)
