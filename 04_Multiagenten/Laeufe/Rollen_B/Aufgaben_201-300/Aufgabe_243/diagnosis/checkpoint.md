Progress: Fault localization complete. Inspected lib/kube/proxy/forwarder.go, forwarder_test.go, and lib/kube/utils/utils.go. No project source or tests changed.

Findings:
- newClusterSessionSameCluster (forwarder.go:1454-1487) calls GetKubeServices and requires a matching registration before consulting f.creds, except when no services exist and kubeCluster equals teleport cluster name. Thus local credentials for another cluster can be ignored and session creation returns NotFound.
- newClusterSession (1418-1423) has no explicit kubeCluster validation; remote sessions with empty kubeCluster succeed, as TestNewClusterSession currently expects (forwarder_test.go:649-667). Clarify intended validation scope when fixing.
- dialWithEndpoints (1391-1415) guards empty endpoints with BadParameter and chooses/falls back among shuffled entries, but mutates teleportCluster.targetAddr/serverID during dialing. setupForwardingHeaders (1123-1125) uses LocalKubernetes when targetAddr is empty, so request URL and selected endpoint may diverge. Existing tests check single and multiple endpoint selection but not missing endpoints, dial failure, or header consistency.
- Remote sessions (1425-1451) use LocalKubernetes and getOrRequestClientCreds; requestCertificate sets RootCAs (1726-1735). Local sessions (1490-1529) use creds targetAddr/tlsConfig. Discovery constructs endpoint addr and serverID name.cluster (1465-1478).
- Requested dialEndpoint/kubeClusterEndpoint/kubeAddress API is absent; current names are DialWithContext, endpoint, and teleportCluster.targetAddr.
