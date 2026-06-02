# drivers/spi/spi-imx.c

Subsystem: drivers/spi

## Functions (77)

### is_imx27_cspi
- Return type: static int
- Signature: is_imx27_cspi(struct spi_imx_data * d)
- Line: 151

### is_imx35_cspi
- Return type: static int
- Signature: is_imx35_cspi(struct spi_imx_data * d)
- Line: 156

### is_imx51_ecspi
- Return type: static int
- Signature: is_imx51_ecspi(struct spi_imx_data * d)
- Line: 161

### is_imx53_ecspi
- Return type: static int
- Signature: is_imx53_ecspi(struct spi_imx_data * d)
- Line: 166

### mx1_intctrl
- Return type: static void
- Signature: mx1_intctrl(struct spi_imx_data * spi_imx,int enable)
- Line: 1045

### mx1_prepare_message
- Return type: static int
- Signature: mx1_prepare_message(struct spi_imx_data * spi_imx,struct spi_message * msg)
- Line: 1066

### mx1_prepare_transfer
- Return type: static int
- Signature: mx1_prepare_transfer(struct spi_imx_data * spi_imx,struct spi_device * spi,struct spi_transfer * t)
- Line: 1072

### mx1_reset
- Return type: static void
- Signature: mx1_reset(struct spi_imx_data * spi_imx)
- Line: 1099

### mx1_rx_available
- Return type: static int
- Signature: mx1_rx_available(struct spi_imx_data * spi_imx)
- Line: 1094

### mx1_trigger
- Return type: static void
- Signature: mx1_trigger(struct spi_imx_data * spi_imx)
- Line: 1057

### mx21_intctrl
- Return type: static void
- Signature: mx21_intctrl(struct spi_imx_data * spi_imx,int enable)
- Line: 970

### mx21_prepare_message
- Return type: static int
- Signature: mx21_prepare_message(struct spi_imx_data * spi_imx,struct spi_message * msg)
- Line: 991

### mx21_prepare_transfer
- Return type: static int
- Signature: mx21_prepare_transfer(struct spi_imx_data * spi_imx,struct spi_device * spi,struct spi_transfer * t)
- Line: 997

### mx21_reset
- Return type: static void
- Signature: mx21_reset(struct spi_imx_data * spi_imx)
- Line: 1029

### mx21_rx_available
- Return type: static int
- Signature: mx21_rx_available(struct spi_imx_data * spi_imx)
- Line: 1024

### mx21_trigger
- Return type: static void
- Signature: mx21_trigger(struct spi_imx_data * spi_imx)
- Line: 982

### mx31_intctrl
- Return type: static void
- Signature: mx31_intctrl(struct spi_imx_data * spi_imx,int enable)
- Line: 866

### mx31_prepare_message
- Return type: static int
- Signature: mx31_prepare_message(struct spi_imx_data * spi_imx,struct spi_message * msg)
- Line: 887

### mx31_prepare_transfer
- Return type: static int
- Signature: mx31_prepare_transfer(struct spi_imx_data * spi_imx,struct spi_device * spi,struct spi_transfer * t)
- Line: 893

### mx31_reset
- Return type: static void
- Signature: mx31_reset(struct spi_imx_data * spi_imx)
- Line: 950

### mx31_rx_available
- Return type: static int
- Signature: mx31_rx_available(struct spi_imx_data * spi_imx)
- Line: 945

### mx31_trigger
- Return type: static void
- Signature: mx31_trigger(struct spi_imx_data * spi_imx)
- Line: 878

### mx51_configure_cpha
- Return type: static void
- Signature: mx51_configure_cpha(struct spi_imx_data * spi_imx,struct spi_device * spi)
- Line: 703

### mx51_ecspi_channel
- Return type: static int
- Signature: mx51_ecspi_channel(const struct spi_device * spi)
- Line: 591

### mx51_ecspi_clkdiv
- Return type: static unsigned int
- Signature: mx51_ecspi_clkdiv(struct spi_imx_data * spi_imx,unsigned int fspi,unsigned int * fres)
- Line: 514

### mx51_ecspi_disable
- Return type: static void
- Signature: mx51_ecspi_disable(struct spi_imx_data * spi_imx)
- Line: 582

### mx51_ecspi_intctrl
- Return type: static void
- Signature: mx51_ecspi_intctrl(struct spi_imx_data * spi_imx,int enable)
- Line: 551

### mx51_ecspi_prepare_message
- Return type: static int
- Signature: mx51_ecspi_prepare_message(struct spi_imx_data * spi_imx,struct spi_message * msg)
- Line: 598

### mx51_ecspi_prepare_transfer
- Return type: static int
- Signature: mx51_ecspi_prepare_transfer(struct spi_imx_data * spi_imx,struct spi_device * spi,struct spi_transfer * t)
- Line: 722

### mx51_ecspi_reset
- Return type: static void
- Signature: mx51_ecspi_reset(struct spi_imx_data * spi_imx)
- Line: 828

### mx51_ecspi_rx_available
- Return type: static int
- Signature: mx51_ecspi_rx_available(struct spi_imx_data * spi_imx)
- Line: 823

### mx51_ecspi_trigger
- Return type: static void
- Signature: mx51_ecspi_trigger(struct spi_imx_data * spi_imx)
- Line: 567

### mx51_setup_wml
- Return type: static void
- Signature: mx51_setup_wml(struct spi_imx_data * spi_imx)
- Line: 807

### mx53_ecspi_rx_target
- Return type: static void
- Signature: mx53_ecspi_rx_target(struct spi_imx_data * spi_imx)
- Line: 457

### mx53_ecspi_tx_target
- Return type: static void
- Signature: mx53_ecspi_tx_target(struct spi_imx_data * spi_imx)
- Line: 484

### spi_imx_buf_rx_swap
- Return type: static void
- Signature: spi_imx_buf_rx_swap(struct spi_imx_data * spi_imx)
- Line: 377

### spi_imx_buf_rx_swap_u32
- Return type: static void
- Signature: spi_imx_buf_rx_swap_u32(struct spi_imx_data * spi_imx)
- Line: 356

### spi_imx_buf_tx_swap
- Return type: static void
- Signature: spi_imx_buf_tx_swap(struct spi_imx_data * spi_imx)
- Line: 429

### spi_imx_buf_tx_swap_u32
- Return type: static void
- Signature: spi_imx_buf_tx_swap_u32(struct spi_imx_data * spi_imx)
- Line: 405

### spi_imx_bytes_per_word
- Return type: static int
- Signature: spi_imx_bytes_per_word(const int bits_per_word)
- Line: 246

### spi_imx_calculate_timeout
- Return type: static int
- Signature: spi_imx_calculate_timeout(struct spi_imx_data * spi_imx,int size)
- Line: 1453

### spi_imx_can_dma
- Return type: static bool
- Signature: spi_imx_can_dma(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 256

### spi_imx_clkdiv_1
- Return type: static unsigned int
- Signature: spi_imx_clkdiv_1(unsigned int fin,unsigned int fspi,unsigned int max,unsigned int * fres)
- Line: 216

### spi_imx_clkdiv_2
- Return type: static unsigned int
- Signature: spi_imx_clkdiv_2(unsigned int fin,unsigned int fspi,unsigned int * fres)
- Line: 230

### spi_imx_dma_configure
- Return type: static int
- Signature: spi_imx_dma_configure(struct spi_controller * controller,bool word_delay)
- Line: 1848

### spi_imx_dma_data_prepare
- Return type: static int
- Signature: spi_imx_dma_data_prepare(struct spi_imx_data * spi_imx,struct spi_transfer * transfer,bool word_delay)
- Line: 1628

### spi_imx_dma_map
- Return type: static int
- Signature: spi_imx_dma_map(struct spi_imx_data * spi_imx,struct dma_data_package * dma_data)
- Line: 1525

### spi_imx_dma_max_wml_find
- Return type: static void
- Signature: spi_imx_dma_max_wml_find(struct spi_imx_data * spi_imx,struct dma_data_package * dma_data,bool word_delay)
- Line: 1828

### spi_imx_dma_package_transfer
- Return type: static int
- Signature: spi_imx_dma_package_transfer(struct spi_imx_data * spi_imx,struct dma_data_package * dma_data,struct spi_transfer * transfer,bool word_delay)
- Line: 1896

### spi_imx_dma_rx_callback
- Return type: static void
- Signature: spi_imx_dma_rx_callback(void * cookie)
- Line: 1439

### spi_imx_dma_rx_data_handle
- Return type: static void
- Signature: spi_imx_dma_rx_data_handle(struct spi_imx_data * spi_imx,struct dma_data_package * dma_data,void * rx_buf,bool word_delay)
- Line: 1481

### spi_imx_dma_submit
- Return type: static int
- Signature: spi_imx_dma_submit(struct spi_imx_data * spi_imx,struct dma_data_package * dma_data,struct spi_transfer * transfer)
- Line: 1717

### spi_imx_dma_transfer
- Return type: static int
- Signature: spi_imx_dma_transfer(struct spi_imx_data * spi_imx,struct spi_transfer * transfer)
- Line: 1935

### spi_imx_dma_tx_callback
- Return type: static void
- Signature: spi_imx_dma_tx_callback(void * cookie)
- Line: 1446

### spi_imx_dma_tx_data_handle
- Return type: static int
- Signature: spi_imx_dma_tx_data_handle(struct spi_imx_data * spi_imx,struct dma_data_package * dma_data,const void * tx_buf,bool word_delay)
- Line: 1557

### spi_imx_dma_unmap
- Return type: static void
- Signature: spi_imx_dma_unmap(struct spi_imx_data * spi_imx,struct dma_data_package * dma_data)
- Line: 1467

### spi_imx_isr
- Return type: static irqreturn_t
- Signature: spi_imx_isr(int irq,void * dev_id)
- Line: 1286

### spi_imx_pio_transfer
- Return type: static int
- Signature: spi_imx_pio_transfer(struct spi_device * spi,struct spi_transfer * transfer)
- Line: 1986

### spi_imx_pio_transfer_target
- Return type: static int
- Signature: spi_imx_pio_transfer_target(struct spi_device * spi,struct spi_transfer * transfer)
- Line: 2066

### spi_imx_poll_transfer
- Return type: static int
- Signature: spi_imx_poll_transfer(struct spi_device * spi,struct spi_transfer * transfer)
- Line: 2018

### spi_imx_prepare_message
- Return type: static int
- Signature: spi_imx_prepare_message(struct spi_controller * controller,struct spi_message * msg)
- Line: 2180

### spi_imx_probe
- Return type: static int
- Signature: spi_imx_probe(struct platform_device * pdev)
- Line: 2218

### spi_imx_push
- Return type: static void
- Signature: spi_imx_push(struct spi_imx_data * spi_imx)
- Line: 1246

### spi_imx_remove
- Return type: static void
- Signature: spi_imx_remove(struct platform_device * pdev)
- Line: 2385

### spi_imx_resume
- Return type: static int
- Signature: spi_imx_resume(struct device * dev)
- Line: 2446

### spi_imx_runtime_resume
- Return type: static int
- Signature: spi_imx_runtime_resume(struct device * dev)
- Line: 2406

### spi_imx_runtime_suspend
- Return type: static int
- Signature: spi_imx_runtime_suspend(struct device * dev)
- Line: 2427

### spi_imx_sdma_exit
- Return type: static void
- Signature: spi_imx_sdma_exit(struct spi_imx_data * spi_imx)
- Line: 1388

### spi_imx_sdma_init
- Return type: static int
- Signature: spi_imx_sdma_init(struct device * dev,struct spi_imx_data * spi_imx,struct spi_controller * controller)
- Line: 1403

### spi_imx_set_burst_len
- Return type: static void
- Signature: spi_imx_set_burst_len(struct spi_imx_data * spi_imx,int n_bits)
- Line: 1236

### spi_imx_setup
- Return type: static int
- Signature: spi_imx_setup(struct spi_device * spi)
- Line: 2171

### spi_imx_setupxfer
- Return type: static int
- Signature: spi_imx_setupxfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 1316

### spi_imx_suspend
- Return type: static int
- Signature: spi_imx_suspend(struct device * dev)
- Line: 2440

### spi_imx_target_abort
- Return type: static int
- Signature: spi_imx_target_abort(struct spi_controller * controller)
- Line: 2208

### spi_imx_transfer_estimate_time_us
- Return type: static unsigned int
- Signature: spi_imx_transfer_estimate_time_us(struct spi_transfer * transfer)
- Line: 2109

### spi_imx_transfer_one
- Return type: static int
- Signature: spi_imx_transfer_one(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 2128

### spi_imx_unprepare_message
- Return type: static int
- Signature: spi_imx_unprepare_message(struct spi_controller * controller,struct spi_message * msg)
- Line: 2200

## Structs (3)

### dma_data_package
- Line: 99
- Members:
  - intctrl: void (*)(struct spi_imx_data * spi_imx,int enable)
  - prepare_message: int (*)(struct spi_imx_data * spi_imx,struct spi_message * msg)
  - prepare_transfer: int (*)(struct spi_imx_data * spi_imx,struct spi_device * spi,struct spi_transfer * t)
  - trigger: void (*)(struct spi_imx_data * spi_imx)
  - rx_available: int (*)(struct spi_imx_data * spi_imx)
  - reset: void (*)(struct spi_imx_data * spi_imx)
  - setup_wml: void (*)(struct spi_imx_data * spi_imx)
  - disable: void (*)(struct spi_imx_data * spi_imx)
  - has_dmamode: bool
  - has_targetmode: bool
  - fifo_size: unsigned int
  - dynamic_burst: bool
  - tx_glitch_fixed: bool
  - devtype: spi_imx_devtype
  - cmd_word: u32
  - dma_rx_buf: void *
  - dma_tx_buf: void *
  - dma_tx_addr: dma_addr_t
  - dma_rx_addr: dma_addr_t
  - dma_len: int
  - data_len: int
  - controller: spi_controller *
  - dev: device *
  - xfer_done: completion
  - base: void __iomem *
  - base_phys: unsigned long
  - clk_per: clk *
  - clk_ipg: clk *
  - spi_clk: unsigned long
  - spi_bus_clk: unsigned int
  - bits_per_word: unsigned int
  - spi_drctl: unsigned int
  - count: unsigned int
  - remainder: unsigned int
  - tx: void (*)(struct spi_imx_data * spi_imx)
  - rx: void (*)(struct spi_imx_data * spi_imx)
  - rx_buf: void *
  - tx_buf: const void *
  - txfifo: unsigned int
  - dynamic_burst: unsigned int
  - rx_only: bool
  - target_mode: bool
  - target_aborted: bool
  - target_burst: unsigned int
  - usedma: bool
  - wml: u32
  - dma_rx_completion: completion
  - dma_tx_completion: completion
  - dma_package_num: size_t
  - dma_data: dma_data_package *
  - rx_offset: int
  - devtype_data: const struct spi_imx_devtype_data *

### spi_imx_data
- Line: 109
- Members:
  - intctrl: void (*)(struct spi_imx_data * spi_imx,int enable)
  - prepare_message: int (*)(struct spi_imx_data * spi_imx,struct spi_message * msg)
  - prepare_transfer: int (*)(struct spi_imx_data * spi_imx,struct spi_device * spi,struct spi_transfer * t)
  - trigger: void (*)(struct spi_imx_data * spi_imx)
  - rx_available: int (*)(struct spi_imx_data * spi_imx)
  - reset: void (*)(struct spi_imx_data * spi_imx)
  - setup_wml: void (*)(struct spi_imx_data * spi_imx)
  - disable: void (*)(struct spi_imx_data * spi_imx)
  - has_dmamode: bool
  - has_targetmode: bool
  - fifo_size: unsigned int
  - dynamic_burst: bool
  - tx_glitch_fixed: bool
  - devtype: spi_imx_devtype
  - cmd_word: u32
  - dma_rx_buf: void *
  - dma_tx_buf: void *
  - dma_tx_addr: dma_addr_t
  - dma_rx_addr: dma_addr_t
  - dma_len: int
  - data_len: int
  - controller: spi_controller *
  - dev: device *
  - xfer_done: completion
  - base: void __iomem *
  - base_phys: unsigned long
  - clk_per: clk *
  - clk_ipg: clk *
  - spi_clk: unsigned long
  - spi_bus_clk: unsigned int
  - bits_per_word: unsigned int
  - spi_drctl: unsigned int
  - count: unsigned int
  - remainder: unsigned int
  - tx: void (*)(struct spi_imx_data * spi_imx)
  - rx: void (*)(struct spi_imx_data * spi_imx)
  - rx_buf: void *
  - tx_buf: const void *
  - txfifo: unsigned int
  - dynamic_burst: unsigned int
  - rx_only: bool
  - target_mode: bool
  - target_aborted: bool
  - target_burst: unsigned int
  - usedma: bool
  - wml: u32
  - dma_rx_completion: completion
  - dma_tx_completion: completion
  - dma_package_num: size_t
  - dma_data: dma_data_package *
  - rx_offset: int
  - devtype_data: const struct spi_imx_devtype_data *

### spi_imx_devtype_data
- Line: 77
- Members:
  - intctrl: void (*)(struct spi_imx_data * spi_imx,int enable)
  - prepare_message: int (*)(struct spi_imx_data * spi_imx,struct spi_message * msg)
  - prepare_transfer: int (*)(struct spi_imx_data * spi_imx,struct spi_device * spi,struct spi_transfer * t)
  - trigger: void (*)(struct spi_imx_data * spi_imx)
  - rx_available: int (*)(struct spi_imx_data * spi_imx)
  - reset: void (*)(struct spi_imx_data * spi_imx)
  - setup_wml: void (*)(struct spi_imx_data * spi_imx)
  - disable: void (*)(struct spi_imx_data * spi_imx)
  - has_dmamode: bool
  - has_targetmode: bool
  - fifo_size: unsigned int
  - dynamic_burst: bool
  - tx_glitch_fixed: bool
  - devtype: spi_imx_devtype
  - cmd_word: u32
  - dma_rx_buf: void *
  - dma_tx_buf: void *
  - dma_tx_addr: dma_addr_t
  - dma_rx_addr: dma_addr_t
  - dma_len: int
  - data_len: int
  - controller: spi_controller *
  - dev: device *
  - xfer_done: completion
  - base: void __iomem *
  - base_phys: unsigned long
  - clk_per: clk *
  - clk_ipg: clk *
  - spi_clk: unsigned long
  - spi_bus_clk: unsigned int
  - bits_per_word: unsigned int
  - spi_drctl: unsigned int
  - count: unsigned int
  - remainder: unsigned int
  - tx: void (*)(struct spi_imx_data * spi_imx)
  - rx: void (*)(struct spi_imx_data * spi_imx)
  - rx_buf: void *
  - tx_buf: const void *
  - txfifo: unsigned int
  - dynamic_burst: unsigned int
  - rx_only: bool
  - target_mode: bool
  - target_aborted: bool
  - target_burst: unsigned int
  - usedma: bool
  - wml: u32
  - dma_rx_completion: completion
  - dma_tx_completion: completion
  - dma_package_num: size_t
  - dma_data: dma_data_package *
  - rx_offset: int
  - devtype_data: const struct spi_imx_devtype_data *

## Enums (1)

### spi_imx_devtype
- Line: 65

## Variables (13)

- static **imx1_cspi_devtype_data** : spi_imx_devtype_data (line 1104)
- static **imx21_cspi_devtype_data** : spi_imx_devtype_data (line 1118)
- static **imx27_cspi_devtype_data** : spi_imx_devtype_data (line 1132)
- static **imx31_cspi_devtype_data** : spi_imx_devtype_data (line 1147)
- static **imx35_cspi_devtype_data** : spi_imx_devtype_data (line 1161)
- static **imx51_ecspi_devtype_data** : spi_imx_devtype_data (line 1176)
- static **imx53_ecspi_devtype_data** : spi_imx_devtype_data (line 1192)
- static **imx6ul_ecspi_devtype_data** : spi_imx_devtype_data (line 1206)
- static **imx_spi_pm** : const struct dev_pm_ops (line 2452)
- static **polling_limit_us** : unsigned int (line 39)
- static **spi_imx_driver** : platform_driver (line 2457)
- static **spi_imx_dt_ids** : const struct of_device_id[] (line 1223)
- static **use_dma** : bool (line 34)

## Macros (96)

- **BYTES_PER_32BITS_WORD** (line 63)
- **DMA_CACHE_ALIGNED_LEN**(x) (line 207)
- **DRIVER_NAME** (line 32)
- **MAX_SDMA_BD_BYTES** (line 59)
- **MX1_CSPICTRL_DR_SHIFT** (line 1043)
- **MX1_CSPICTRL_ENABLE** (line 1041)
- **MX1_CSPICTRL_HOST** (line 1042)
- **MX1_CSPICTRL_PHA** (line 1039)
- **MX1_CSPICTRL_POL** (line 1038)
- **MX1_CSPICTRL_XCH** (line 1040)
- **MX1_INTREG_RR** (line 1034)
- **MX1_INTREG_RREN** (line 1036)
- **MX1_INTREG_TEEN** (line 1035)
- **MX21_CSPICTRL_CS_SHIFT** (line 968)
- **MX21_CSPICTRL_DR_SHIFT** (line 967)
- **MX21_CSPICTRL_ENABLE** (line 965)
- **MX21_CSPICTRL_HOST** (line 966)
- **MX21_CSPICTRL_PHA** (line 962)
- **MX21_CSPICTRL_POL** (line 961)
- **MX21_CSPICTRL_SSPOL** (line 963)
- **MX21_CSPICTRL_XCH** (line 964)
- **MX21_INTREG_RR** (line 957)
- **MX21_INTREG_RREN** (line 959)
- **MX21_INTREG_TEEN** (line 958)
- **MX31_CSPICTRL_BC_SHIFT** (line 846)
- **MX31_CSPICTRL_CS_SHIFT** (line 848)
- **MX31_CSPICTRL_DR_SHIFT** (line 850)
- **MX31_CSPICTRL_ENABLE** (line 838)
- **MX31_CSPICTRL_HOST** (line 839)
- **MX31_CSPICTRL_PHA** (line 843)
- **MX31_CSPICTRL_POL** (line 842)
- **MX31_CSPICTRL_SMC** (line 841)
- **MX31_CSPICTRL_SSCTL** (line 844)
- **MX31_CSPICTRL_SSPOL** (line 845)
- **MX31_CSPICTRL_XCH** (line 840)
- **MX31_CSPISTATUS** (line 856)
- **MX31_CSPI_DMAREG** (line 852)
- **MX31_CSPI_TESTREG** (line 859)
- **MX31_DMAREG_RH_DEN** (line 853)
- **MX31_DMAREG_TH_DEN** (line 854)
- **MX31_INTREG_RREN** (line 836)
- **MX31_INTREG_TEEN** (line 835)
- **MX31_STATUS_RR** (line 857)
- **MX31_TEST_LBC** (line 860)
- **MX35_CSPICTRL_BL_SHIFT** (line 847)
- **MX35_CSPICTRL_CS_SHIFT** (line 849)
- **MX51_ECSPI_CONFIG** (line 316)
- **MX51_ECSPI_CONFIG_DATACTL**(cs) (line 321)
- **MX51_ECSPI_CONFIG_SBBCTRL**(cs) (line 319)
- **MX51_ECSPI_CONFIG_SCLKCTL**(cs) (line 322)
- **MX51_ECSPI_CONFIG_SCLKPHA**(cs) (line 317)
- **MX51_ECSPI_CONFIG_SCLKPOL**(cs) (line 318)
- **MX51_ECSPI_CONFIG_SSBPOL**(cs) (line 320)
- **MX51_ECSPI_CTRL** (line 304)
- **MX51_ECSPI_CTRL_BL_MASK** (line 314)
- **MX51_ECSPI_CTRL_BL_OFFSET** (line 313)
- **MX51_ECSPI_CTRL_CS**(cs) (line 312)
- **MX51_ECSPI_CTRL_DRCTL**(drctl) (line 309)
- **MX51_ECSPI_CTRL_ENABLE** (line 305)
- **MX51_ECSPI_CTRL_MAX_BURST** (line 60)
- **MX51_ECSPI_CTRL_MODE_MASK** (line 308)
- **MX51_ECSPI_CTRL_POSTDIV_OFFSET** (line 310)
- **MX51_ECSPI_CTRL_PREDIV_OFFSET** (line 311)
- **MX51_ECSPI_CTRL_SMC** (line 307)
- **MX51_ECSPI_CTRL_XCH** (line 306)
- **MX51_ECSPI_DMA** (line 329)
- **MX51_ECSPI_DMA_RXDEN** (line 335)
- **MX51_ECSPI_DMA_RXTDEN** (line 336)
- **MX51_ECSPI_DMA_RXT_WML**(wml) (line 332)
- **MX51_ECSPI_DMA_RX_WML**(wml) (line 331)
- **MX51_ECSPI_DMA_TEDEN** (line 334)
- **MX51_ECSPI_DMA_TX_WML**(wml) (line 330)
- **MX51_ECSPI_INT** (line 324)
- **MX51_ECSPI_INT_RDREN** (line 327)
- **MX51_ECSPI_INT_RREN** (line 326)
- **MX51_ECSPI_INT_TEEN** (line 325)
- **MX51_ECSPI_PERIOD** (line 341)
- **MX51_ECSPI_PERIOD_MASK** (line 342)
- **MX51_ECSPI_PERIOD_MIN_DELAY_SCK** (line 351)
- **MX51_ECSPI_STAT** (line 338)
- **MX51_ECSPI_STAT_RR** (line 339)
- **MX51_ECSPI_TESTREG** (line 353)
- **MX51_ECSPI_TESTREG_LBC** (line 354)
- **MX53_MAX_TRANSFER_BYTES** (line 62)
- **MXC_CSPICTRL** (line 49)
- **MXC_CSPIINT** (line 50)
- **MXC_CSPIRXDATA** (line 47)
- **MXC_CSPITXDATA** (line 48)
- **MXC_INT_RDR** (line 56)
- **MXC_INT_RR** (line 54)
- **MXC_INT_TE** (line 55)
- **MXC_RESET** (line 51)
- **MXC_RPM_TIMEOUT** (line 44)
- **MXC_SPI_BUF_RX**(type) (line 171)
- **MXC_SPI_BUF_TX**(type) (line 184)
- **MXC_SPI_DEFAULT_SPEED** (line 45)
