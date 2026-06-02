# drivers/spi/spi-loopback-test.c

Subsystem: drivers/spi

## Functions (14)

### _spi_test_run_iter
- Return type: static int
- Signature: _spi_test_run_iter(struct spi_device * spi,struct spi_test * test,void * tx,void * rx)
- Line: 791

### rx_ranges_cmp
- Return type: static int
- Signature: rx_ranges_cmp(void * priv,const struct list_head * a,const struct list_head * b)
- Line: 494

### spi_check_rx_ranges
- Return type: static int
- Signature: spi_check_rx_ranges(struct spi_device * spi,struct spi_message * msg,void * rx)
- Line: 507

### spi_loopback_test_probe
- Return type: static int
- Signature: spi_loopback_test_probe(struct spi_device * spi)
- Line: 358

### spi_test_check_elapsed_time
- Return type: static int
- Signature: spi_test_check_elapsed_time(struct spi_device * spi,struct spi_test * test)
- Line: 572

### spi_test_check_loopback_result
- Return type: static int
- Signature: spi_test_check_loopback_result(struct spi_device * spi,struct spi_message * msg,void * tx,void * rx)
- Line: 602

### spi_test_dump_message
- Return type: static void
- Signature: spi_test_dump_message(struct spi_device * spi,struct spi_message * msg,bool dump_data)
- Line: 441

### spi_test_execute_msg
- Return type: int
- Signature: spi_test_execute_msg(struct spi_device * spi,struct spi_test * test,void * tx,void * rx)
- Line: 933

### spi_test_fill_pattern
- Return type: static int
- Signature: spi_test_fill_pattern(struct spi_device * spi,struct spi_test * test)
- Line: 707

### spi_test_print_hex_dump
- Return type: static void
- Signature: spi_test_print_hex_dump(char * pre,const void * ptr,size_t len)
- Line: 420

### spi_test_run_iter
- Return type: static int
- Signature: spi_test_run_iter(struct spi_device * spi,const struct spi_test * testtemplate,void * tx,void * rx,size_t len,size_t tx_off,size_t rx_off)
- Line: 853

### spi_test_run_test
- Return type: int
- Signature: spi_test_run_test(struct spi_device * spi,const struct spi_test * test,void * tx,void * rx)
- Line: 1006

### spi_test_run_tests
- Return type: int
- Signature: spi_test_run_tests(struct spi_device * spi,struct spi_test * tests)
- Line: 1069

### spi_test_translate
- Return type: static int
- Signature: spi_test_translate(struct spi_device * spi,void ** ptr,size_t len,void * tx,void * rx)
- Line: 664

## Structs (1)

### rx_ranges
- Line: 488
- Members:
  - list: list_head
  - start: u8 *
  - end: u8 *

## Variables (13)

- static **check_ranges** : int (line 75)
- static **delay_ms** : unsigned int (line 80)
- static **dump_messages** : int (line 31)
- static **loop_req** : int (line 45)
- static **loopback** : int (line 38)
- static **no_cs** : int (line 51)
- static **run_only_iter_len** : int (line 57)
- static **run_only_test** : int (line 63)
- static **simulate_only** : int (line 26)
- static **spi_loopback_test_driver** : spi_driver (line 396)
- static **spi_loopback_test_of_match** : of_device_id[] (line 384)
- static **spi_tests** : spi_test[] (line 86)
- static **use_vmalloc** : int (line 69)

## Macros (5)

- **FOR_EACH_ALIGNMENT**(var) (line 1030)
- **GET_VALUE_BYTE**(value,index,bytes) (line 716)
- **GET_VALUE_BYTE**(value,index,bytes) (line 719)
- **RANGE_CHECK**(ptr,plen,start,slen) (line 414)
- **SPI_TEST_MAX_SIZE_PLUS** (line 418)
