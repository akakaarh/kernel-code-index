# drivers/mmc/host/mmci_qcom_dml.c

Subsystem: drivers/mmc

## Functions (5)

### of_get_dml_pipe_index
- Return type: static int
- Signature: of_get_dml_pipe_index(struct device_node * np,const char * name)
- Line: 98

### qcom_dma_setup
- Return type: static int
- Signature: qcom_dma_setup(struct mmci_host * host)
- Line: 120

### qcom_dma_start
- Return type: static int
- Signature: qcom_dma_start(struct mmci_host * host,unsigned int * datactrl)
- Line: 48

### qcom_get_dctrl_cfg
- Return type: static u32
- Signature: qcom_get_dctrl_cfg(struct mmci_host * host)
- Line: 183

### qcom_variant_init
- Return type: void
- Signature: qcom_variant_init(struct mmci_host * host)
- Line: 200

## Variables (1)

- static **qcom_variant_ops** : mmci_host_ops (line 188)

## Macros (28)

- **BYPASS** (line 24)
- **CONSUMER_CRCI_DISABLE** (line 20)
- **CONSUMER_CRCI_MSK** (line 19)
- **CONSUMER_CRCI_X_SEL** (line 21)
- **CONSUMER_CRCI_Y_SEL** (line 22)
- **CONSUMER_PIPE_ID_MSK** (line 37)
- **CONSUMER_PIPE_ID_SHFT** (line 36)
- **CONSUMER_PIPE_LOGICAL_SIZE** (line 44)
- **DIRECT_MODE** (line 25)
- **DML_CONFIG** (line 14)
- **DML_CONSUMER_PIPE_LOGICAL_SIZE** (line 32)
- **DML_CONSUMER_START** (line 30)
- **DML_OFFSET** (line 46)
- **DML_PIPE_ID** (line 33)
- **DML_PRODUCER_BAM_BLOCK_SIZE** (line 39)
- **DML_PRODUCER_BAM_TRANS_SIZE** (line 40)
- **DML_PRODUCER_PIPE_LOGICAL_SIZE** (line 31)
- **DML_PRODUCER_START** (line 29)
- **DML_SW_RESET** (line 28)
- **INFINITE_CONS_TRANS** (line 26)
- **PRODUCER_CRCI_DISABLE** (line 16)
- **PRODUCER_CRCI_MSK** (line 15)
- **PRODUCER_CRCI_X_SEL** (line 17)
- **PRODUCER_CRCI_Y_SEL** (line 18)
- **PRODUCER_PIPE_ID_MSK** (line 35)
- **PRODUCER_PIPE_ID_SHFT** (line 34)
- **PRODUCER_PIPE_LOGICAL_SIZE** (line 43)
- **PRODUCER_TRANS_END_EN** (line 23)
