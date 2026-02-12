# Giteagle Demo: Kubernetes Ecosystem

> **Generated on 2026-02-12 00:01:01 UTC**
>
> This demo showcases giteagle by querying real activity across the
> [Kubernetes](https://github.com/kubernetes) GitHub organization.
> All output below is live data from the GitHub API — nothing is pre-recorded or faked.

---

## 1. Show Configuration

Display the current giteagle configuration, including which platform tokens are configured.

```bash
$ uv run giteagle config
```

```
            Configuration            
╭─────────────────────────┬─────────╮
│ Setting                 │ Value   │
├─────────────────────────┼─────────┤
│ Default Platform        │ github  │
│ Cache TTL               │ 300s    │
│ Max Concurrent Requests │ 10      │
│ GitHub Token            │ ***     │
│ GitLab Token            │ Not set │
│ Bitbucket Token         │ Not set │
╰─────────────────────────┴─────────╯

Set tokens via GITHUB_TOKEN, GITLAB_TOKEN, BITBUCKET_TOKEN environment variables
```


## 2. List Kubernetes Organization Repos

List public repositories in the Kubernetes GitHub organization.

```bash
$ uv run giteagle repos kubernetes --org
```

```
                                            Repositories for kubernetes                                            
╭──────────────────────────────┬───────────────────────────────────────────────────────┬────────────────┬─────────╮
│ Name                         │ Description                                           │ Default Branch │ Private │
├──────────────────────────────┼───────────────────────────────────────────────────────┼────────────────┼─────────┤
│ kubernetes                   │ Production-Grade Container Scheduling and Manageme... │ master         │ No      │
│ website                      │ Kubernetes website and documentation repo:            │ main           │ No      │
│ release                      │ Release infrastructure for Kubernetes and related ... │ master         │ No      │
│ minikube                     │ Run Kubernetes locally                                │ master         │ No      │
│ test-infra                   │ Test infrastructure for the Kubernetes project.       │ master         │ No      │
│ enhancements                 │ Enhancements tracking repo for Kubernetes             │ master         │ No      │
│ community                    │ Kubernetes community content                          │ master         │ No      │
│ kube-state-metrics           │ Add-on agent to generate and expose cluster-level ... │ main           │ No      │
│ node-problem-detector        │ This is a place for various problem detectors runn... │ master         │ No      │
│ kompose                      │ Convert Compose to Kubernetes                         │ main           │ No      │
│ kops                         │ Kubernetes Operations (kOps) - Production Grade k8... │ master         │ No      │
│ kubernetes-template-project  │ A template for starting new projects on the github... │ main           │ No      │
│ git-sync                     │ A sidecar app which clones a git repo and keeps it... │ master         │ No      │
│ k8s.io                       │ Code and configuration to manage Kubernetes projec... │ main           │ No      │
│ client-go                    │ Go client for Kubernetes.                             │ master         │ No      │
│ gengo                        │ gengo library for code generation.                    │ master         │ No      │
│ perf-tests                   │ Performance tests and benchmarks                      │ master         │ No      │
│ ingress-nginx                │ Ingress NGINX Controller for Kubernetes               │ main           │ No      │
│ kubeadm                      │ Aggregator for issues filed against kubeadm           │ main           │ No      │
│ repo-infra                   │ Kubernetes repository infrastucture tools             │ master         │ No      │
│ dns                          │ Kubernetes DNS service                                │ master         │ No      │
│ apimachinery                 │                                                       │ master         │ No      │
│ apiserver                    │ Library for writing a Kubernetes-style API server.    │ master         │ No      │
│ sample-apiserver             │ Reference implementation of an apiserver for a cus... │ master         │ No      │
│ kube-aggregator              │ Aggregator for Kubernetes-style API servers: dynam... │ master         │ No      │
│ metrics                      │ Kubernetes metrics-related API types and clients      │ master         │ No      │
│ kubectl                      │ Issue tracker and mirror of kubectl code              │ master         │ No      │
│ autoscaler                   │ Autoscaling components for Kubernetes                 │ master         │ No      │
│ examples                     │ Kubernetes application example tutorials              │ master         │ No      │
│ api                          │ The canonical location of the Kubernetes API defin... │ master         │ No      │
│ apiextensions-apiserver      │ API server for API extensions like CustomResourceD... │ master         │ No      │
│ utils                        │ Non-Kubernetes-specific utility libraries which ar... │ master         │ No      │
│ kube-openapi                 │ Kubernetes OpenAPI spec generation & serving          │ master         │ No      │
│ sig-release                  │ Repo for SIG release                                  │ master         │ No      │
│ code-generator               │ Generators for kube-like API types                    │ master         │ No      │
│ steering                     │ The Kubernetes Steering Committee                     │ main           │ No      │
│ ingress-gce                  │ Ingress controller for Google Cloud                   │ master         │ No      │
│ sample-controller            │ Repository for sample controller. Complements samp... │ master         │ No      │
│ publishing-bot               │ Code behind the robot to publish from staging to r... │ master         │ No      │
│ cloud-provider-aws           │ Cloud provider for AWS                                │ master         │ No      │
│ cloud-provider-openstack     │                                                       │ master         │ No      │
│ cloud-provider-gcp           │ cloud-provider-gcp contains several projects used ... │ master         │ No      │
│ cloud-provider-vsphere       │ Kubernetes Cloud Provider for vSphere https://clou... │ master         │ No      │
│ org                          │ Meta configuration for Kubernetes Github Org          │ main           │ No      │
│ contributor-site             │ Code for kubernetes.dev                               │ master         │ No      │
│ kube-controller-manager      │ kube-controller-manager component configs             │ master         │ No      │
│ kube-scheduler               │ kube-scheduler component configs                      │ master         │ No      │
│ kubelet                      │ kubelet component configs                             │ master         │ No      │
│ kube-proxy                   │ kube-proxy component configs                          │ master         │ No      │
│ cli-runtime                  │ Set of helpers for creating kubectl commands and p... │ master         │ No      │
│ sample-cli-plugin            │ Sample kubectl plugin                                 │ master         │ No      │
│ cloud-provider-alibaba-cloud │ CloudProvider for Alibaba Cloud                       │ master         │ No      │
│ cluster-bootstrap            │                                                       │ master         │ No      │
│ cloud-provider               │ cloud-provider defines the shared interfaces which... │ master         │ No      │
│ klog                         │ Leveled execution logs for Go (fork of https://git... │ main           │ No      │
│ node-api                     │                                                       │ master         │ No      │
│ cloud-provider-sample        │ Sample of how to build a cloud provider repo. This... │ master         │ No      │
│ component-base               │ Shared code for kubernetes core components            │ master         │ No      │
│ csi-translation-lib          │ Staging repo for CSI Migration/Translation librari... │ master         │ No      │
│ committee-security-response  │ Kubernetes Security Process and Security Committee... │ main           │ No      │
│ cri-api                      │ Container Runtime Interface (CRI) – a plugin inter... │ master         │ No      │
│ legacy-cloud-providers       │ This repository hosts the legacy in-tree cloud pro... │ master         │ No      │
│ system-validators            │ A set of system-oriented validators for kubeadm pr... │ main           │ No      │
│ controller-manager           │ This repo is intended to contain common public lib... │ master         │ No      │
│ mount-utils                  │ Package mount defines an interface to mounting fil... │ master         │ No      │
│ .github                      │ Default files for all repos in the Kubernetes GitH... │ master         │ No      │
│ component-helpers            │ High-level helpers for Kubernetes components          │ master         │ No      │
│ sig-testing                  │ Home for SIG Testing discussion and documents.        │ master         │ No      │
│ pod-security-admission       │ Kubernetes Pod Security Standards implementation -... │ master         │ No      │
│ sig-security                 │ Process documentation, non-code deliverables, and ... │ main           │ No      │
│ design-proposals-archive     │ Archive of Kubernetes Design Proposals                │ main           │ No      │
│ registry.k8s.io              │ This project is the repo for registry.k8s.io, the ... │ main           │ No      │
│ kms                          │ Kubernetes KMS implementation                         │ master         │ No      │
│ dynamic-resource-allocation  │                                                       │ master         │ No      │
│ cel-admission-webhook        │                                                       │ main           │ No      │
│ endpointslice                │                                                       │ master         │ No      │
│ cri-client                   │ Container Runtime Interface client implementation     │ master         │ No      │
│ externaljwt                  │ Synced from kubernetes/kubernetes/staging/external... │ master         │ No      │
╰──────────────────────────────┴───────────────────────────────────────────────────────┴────────────────┴─────────╯

Total: 78 repositories
```


## 3. Recent Activity on kubernetes/kubernetes

Show the 15 most recent activities (commits, pull requests, issues) from the core Kubernetes repository over the last 7 days.

```bash
$ uv run giteagle activity kubernetes/kubernetes --days 7 --limit 15
```

```
╭───────────────────────────────────────────────────────────────────────── Repository ─────────────────────────────────────────────────────────────────────────╮
│ kubernetes/kubernetes                                                                                                                                        │
│ Production-Grade Container Scheduling and Management                                                                                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
                                                Activity (last 7 days)                                                 
╭──────────────┬─────────────────────────────────────────────────────────────────┬─────────────────┬──────────────────╮
│ Type         │ Title                                                           │ Author          │ Date             │
├──────────────┼─────────────────────────────────────────────────────────────────┼─────────────────┼──────────────────┤
│ pull_request │ apiserver: bound checkClient retries and fix DelayFunc data ... │ tobiasworkstech │ 2026-02-11 23:57 │
│ commit       │ Merge pull request #136729 from ahmedtd/podcert-pkcs10          │ k8s-ci-robot    │ 2026-02-11 23:13 │
│ pull_request │ Fix RestartAllContainer restart quickly with single containe... │ yuanwang04      │ 2026-02-11 23:12 │
│ pull_request │ Add tests for RestartAllContainers                              │ yuanwang04      │ 2026-02-11 23:05 │
│ pull_request │ Fix LastTerminationStatus for RestartAllContainers              │ yuanwang04      │ 2026-02-11 23:02 │
│ pull_request │ Keep logs when containers removed by RestartAllContainers       │ yuanwang04      │ 2026-02-11 22:58 │
│ issue        │ kubelet: static pod manifest directory reads ALL non-hidden ... │ yg-codes        │ 2026-02-11 22:57 │
│ pull_request │ Refactor etcd failure test to use nftables with iptables fal... │ kairosci        │ 2026-02-11 22:51 │
│ commit       │ Merge pull request #136796 from kairosci/fix/kube-proxy-nfta... │ k8s-ci-robot    │ 2026-02-11 22:23 │
│ pull_request │ WIP: switch server images to kube-log-runner                    │ BenTheElder     │ 2026-02-11 20:45 │
│ pull_request │ Revert dv native in the validation-gen framework                │ lalitc375       │ 2026-02-11 19:41 │
│ commit       │ pkg/proxy/nftables: fix kube-proxy crash with newer nftables... │ kairosci        │ 2026-02-11 19:00 │
│ commit       │ Merge pull request #133427 from natasha41575/admitHandler       │ k8s-ci-robot    │ 2026-02-11 18:40 │
│ commit       │ Merge pull request #136905 from bart0sh/PR222-e2e-fix-extend... │ k8s-ci-robot    │ 2026-02-11 16:26 │
│ commit       │ Merge pull request #130918 from iPraveenParihar/e2e/add-snap... │ k8s-ci-robot    │ 2026-02-11 13:40 │
╰──────────────┴─────────────────────────────────────────────────────────────────┴─────────────────┴──────────────────╯

Total: 15 activities
```


## 4. Cross-Repository Summary

Aggregate activity across three Kubernetes repositories and break it down by type, top contributors, and per-repository counts.

```bash
$ uv run giteagle summary kubernetes/kubernetes kubernetes/minikube kubernetes/ingress-nginx --days 7
```

```
Fetched 100 activities from kubernetes/kubernetes
Fetched 61 activities from kubernetes/minikube
Fetched 55 activities from kubernetes/ingress-nginx
╭─────────────────────────────────────────────────────────────────── Summary (last 7 days) ────────────────────────────────────────────────────────────────────╮
│ Total Activities: 180                                                                                                                                        │
│ Repositories: 3                                                                                                                                              │
│ Contributors: 56                                                                                                                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
    By Activity Type    
                        
  Type           Count  
 ────────────────────── 
  pull_request      93  
  commit            69  
  issue             18  
                        
             Top Contributors              
                                           
  Username                     Activities  
 ───────────────────────────────────────── 
  k8s-ci-robot                         38  
  k8s-infra-cherrypick-robot           17  
  minikube-bot                         14  
  Gacko                                12  
  dependabot                           10  
                                           
              By Repository              
                                         
  Repository                 Activities  
 ─────────────────────────────────────── 
  kubernetes/kubernetes             100  
  kubernetes/ingress-nginx           51  
  kubernetes/minikube                29  
                                         
```


## 5. Activity Timeline

Visualize weekly activity over the past 30 days across three Kubernetes repositories.

```bash
$ uv run giteagle timeline kubernetes/kubernetes kubernetes/minikube kubernetes/ingress-nginx --days 30 --granularity week
```

```
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Activity Timeline (weekly)                                                                                                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
2026-01-12: █████████████████████████ 209
2026-01-19: █████████████████████ 176
2026-01-26: █████████████████████████████ 239
2026-02-02: ████████████████████████████████████████ 328
2026-02-09: ████████████████████████████ 234
```


## 6. Unified Git Log Across Repos

Browse commits across multiple repositories in a single unified view, like `tig` but for multiple repos. Each repo gets a distinct color, commits are grouped by date, and merge commits are marked.

```bash
$ uv run giteagle log kubernetes/kubernetes kubernetes/minikube kubernetes/ingress-nginx --days 3 --limit 15
```

```
Fetched 6 commits from kubernetes/kubernetes
Fetched 1 commits from kubernetes/minikube
Fetched 4 commits from kubernetes/ingress-nginx
 ● 2026-02-11  ingress-nginx  296ce3b  CI: Update Kubernetes to v1.35.1. (#14561)
 │             kubernetes     54489c1  Merge pull request #136729 from ahmedtd/podcert-pkcs10 (merge)
 │             kubernetes     04d82d9  Merge pull request #136796 from kairosci/fix/kube-proxy-nftables-udata (merge)
 │             ingress-nginx  50faa99  Docs: Clarify PROXY protocol is not supported on GKE default load balancer. (#14558)
 │             kubernetes     72ef5b3  pkg/proxy/nftables: fix kube-proxy crash with newer nftables versions
 │             kubernetes     311071d  Merge pull request #133427 from natasha41575/admitHandler (merge)
 │             kubernetes     7b21ce7  Merge pull request #136905 from bart0sh/PR222-e2e-fix-extended-resource-flake (merge)
 │             kubernetes     8b09f92  Merge pull request #130918 from iPraveenParihar/e2e/add-snapshot-metadata (merge)
 ● 2026-02-10  minikube       f750803  Build(deps): Bump the golang-org group with 6 updates (#22647)
 │             ingress-nginx  efcd54f  Controller: Enable SSL Passthrough when requested on before HTTP-only hosts. (#14555)
 ● 2026-02-09  ingress-nginx  72d99b3  CI: Update Helm to v4.1.1. (#14552)

Total: 11 commits across 3 repositories
```


Filter to a specific contributor:

```bash
$ uv run giteagle log kubernetes/kubernetes kubernetes/minikube --author k8s-ci-robot --days 3
```

```
Fetched 56 commits from kubernetes/kubernetes
Fetched 1 commits from kubernetes/minikube
 ● 2026-02-11  kubernetes  54489c1  Merge pull request #136729 from ahmedtd/podcert-pkcs10 (merge)
 │             kubernetes  04d82d9  Merge pull request #136796 from kairosci/fix/kube-proxy-nftables-udata (merge)
 │             kubernetes  311071d  Merge pull request #133427 from natasha41575/admitHandler (merge)
 │             kubernetes  7b21ce7  Merge pull request #136905 from bart0sh/PR222-e2e-fix-extended-resource-flake (merge)
 │             kubernetes  8b09f92  Merge pull request #130918 from iPraveenParihar/e2e/add-snapshot-metadata (merge)
 │             kubernetes  45b9248  Merge pull request #136719 from pohly/e2e-gce-speedups (merge)
 │             kubernetes  90a76aa  Merge pull request #136846 from carlory/update-cri-losing-support (merge)
 │             kubernetes  9dc55d7  Merge pull request #135729 from yangjunmyfm192085/fixe2e2 (merge)
 │             kubernetes  fce5bc2  Merge pull request #134316 from xigang/node_controller_pod (merge)
 │             kubernetes  a79d324  Merge pull request #136927 from BenTheElder/clean-fix (merge)
 │             kubernetes  7b99981  Merge pull request #136925 from michaelasp/pipeFeatureGate (merge)
 │             kubernetes  b236451  Merge pull request #136928 from BenTheElder/cleanup-unused-env (merge)
 │             kubernetes  46ac9df  Merge pull request #135675 from richabanker/merged-discovery (merge)
 │             kubernetes  eb09a3c  Merge pull request #135395 from pohly/apimachinery-wait-for-cache-sync (merge)
 ● 2026-02-10  kubernetes  99d4b4d  Merge pull request #135256 from natasha41575/pod-gen-field (merge)
 │             kubernetes  870e292  Merge pull request #136716 from yonizxz/concurrent-node-syncs-split (merge)
 │             kubernetes  c9534cb  Merge pull request #134981 from haircommander/drop-cpu-load (merge)
 │             kubernetes  3e15c6f  Merge pull request #136911 from pohly/dra-e2e-data-race (merge)
 │             kubernetes  1bb2e12  Merge pull request #136734 from sunya-ch/sunya-ch/fix-gather-shared-id (merge)
 │             kubernetes  65f09e6  Merge pull request #136826 from alvaroaleman/bumpv0.32 (merge)
 │             kubernetes  e7f26c6  Merge pull request #136339 from ffromani/deprecate-customcpucfsquota-fg-not-feature (merge)
 │             kubernetes  7f890ab  Merge pull request #136802 from pohly/fix-data-race-refs-populaterefs (merge)
 │             kubernetes  2a9b8ba  Merge pull request #136787 from ahmedtd/bump-ctb (merge)
 │             kubernetes  01b283a  Merge pull request #136907 from aojea/ipaddress_flake (merge)
 │             kubernetes  59cdded  Merge pull request #136901 from Phaow/vac-fix (merge)
 │             kubernetes  4670994  Merge pull request #136898 from carlory/kubeadm-ContainerRuntimeVersion-1-37 (merge)
 │             kubernetes  76b4a90  Merge pull request #136326 from bart0sh/PR218-migrate-kubelet_node_status-to-contextual-logging (merge)
 │             kubernetes  65b1000  Merge pull request #135749 from novahe/fix-defer-latency (merge)
 │             kubernetes  44dc4cb  Merge pull request #136888 from neolit123/revert-136130-kubeadm_use_newclientset (merge)
 │             kubernetes  b6f27f1  Merge pull request #136856 from pohly/dra-integration-timeouts (merge)
 │             kubernetes  0bb7533  Merge pull request #135464 from MikeSpreitzer/better-concurrency-test-margin (merge)
 │             kubernetes  1955210  Merge pull request #134044 from mcallzbl/master (merge)
 │             kubernetes  7b0310a  Merge pull request #136820 from dims/update-otel-deps (merge)
 │             kubernetes  f693c45  Merge pull request #136775 from atombrella/feature/activate_modernize_slicessort (merge)
 ● 2026-02-09  kubernetes  fc74562  Merge pull request #136808 from nmn3m/kubelet-contextual-logging (merge)
 │             kubernetes  09e1c9f  Merge pull request #136455 from pohly/client-go-simpleclient-undeprecation (merge)
 │             kubernetes  139e78d  Merge pull request #136337 from pohly/dra-e2e-hostpath-image-selection (merge)
 │             kubernetes  e73221c  Merge pull request #136488 from thockin/fix_bad_arg_name_in_dv (merge)

Total: 38 commits across 1 repositories
```


## 7. Daily Standup Report

Generate a standup-ready summary of recent activity across repositories. The `standup` command groups activities by repo and categorizes them as commits, PRs opened/merged/closed, and issues. Use `--author` to filter by contributor.

```bash
$ uv run giteagle standup kubernetes/kubernetes kubernetes/ingress-nginx --author k8s-ci-robot --days 3
```

```
Fetched 200 activities from kubernetes/kubernetes
Fetched 38 activities from kubernetes/ingress-nginx
Standup for k8s-ci-robot since 2026-02-09 (Mon)
──────────────────────────────────────────────────

kubernetes/kubernetes (40 activities)
  Commits (40): Merge pull request #136729 from ahmedtd/podcert-pk, Merge pull request #136796 from kairosci/fix/kube-, Merge pull request #133427 from 
natasha41575/admit, Merge pull request #136905 from bart0sh/PR222-e2e-, Merge pull request #130918 from iPraveenParihar/e2

Total: 40 activities across 1 repositories
```


## 8. Cross-Repo PR Dashboard

Show all open pull requests across repos with review status, CI status, age, and labels. PRs older than `--stale` days are highlighted as stale.

```bash
$ uv run giteagle prs kubernetes/ingress-nginx --stale 7
```

```
Fetched 44 open PRs from kubernetes/ingress-nginx
                                                                    Open Pull Requests (44)                                                                     
╭───────────────┬───────────────────────────────────────────┬───────────────────────┬──────┬──────────────┬─────────┬──────────────────────────────────────────╮
│ Repo          │ PR                                        │ Author                │ Age  │ Reviews      │ CI      │ Labels                                   │
├───────────────┼───────────────────────────────────────────┼───────────────────────┼──────┼──────────────┼─────────┼──────────────────────────────────────────┤
│ ingress-nginx │ #8366 Allow overriding real_ip_recursive  │ tomaspinho            │ 203w │ pending      │ pending │ cncf-cla: yes, area/docs, size/L         │
│ ingress-nginx │ #8385 feat(annotations): introduce        │ aslafy-z              │ 203w │ pending      │ pending │ cncf-cla: yes, area/docs, size/L         │
│               │ enable-custom-http-er...                  │                       │      │              │         │                                          │
│ ingress-nginx │ #8582 Adds strict match annotation +      │ chrisshino            │ 195w │ changes (1)  │ pending │ cncf-cla: yes, area/docs, size/L         │
│               │ updated tests/docs                        │                       │      │              │         │                                          │
│ ingress-nginx │ #9025 Add least_connections load          │ alowde                │ 179w │ changes (1)  │ pending │ cncf-cla: yes, area/docs, size/XL        │
│               │ balancing algorithm.                      │                       │      │              │         │                                          │
│ ingress-nginx │ #9239 Implement Consistent Hashing with   │ kirs                  │ 171w │ pending      │ pending │ cncf-cla: yes, size/XL, needs-rebase     │
│               │ Bounded Loads                             │                       │      │              │         │                                          │
│ ingress-nginx │ #9586 add default http health check       │ hassenius             │ 157w │ pending      │ pending │ cncf-cla: yes, size/M, needs-kind        │
│ ingress-nginx │ #9977 Fix the error while setting         │ ghostloda             │ 142w │ pending      │ pending │ cncf-cla: yes, size/XS, needs-kind       │
│               │ upstream peer                             │                       │      │              │         │                                          │
│ ingress-nginx │ #10072 fix: issue where canary overwrites │ Spazzy757             │ 139w │ pending      │ pending │ cncf-cla: yes, size/L, kind/bug          │
│               │ default backend                           │                       │      │              │         │                                          │
│ ingress-nginx │ #10454 TCP Proxy: Fix corrupted hostname  │ chotiwat              │ 123w │ pending      │ pending │ cncf-cla: yes, size/L, kind/bug          │
│               │ from partial con...                       │                       │      │              │         │                                          │
│ ingress-nginx │ #10627 support 2 tier control over        │ travisghansen         │ 118w │ pending      │ pending │ cncf-cla: yes, size/M, needs-ok-to-test  │
│               │ sticky_persistent sess...                 │                       │      │              │         │                                          │
│ ingress-nginx │ #10686 Ingress Status: Improve checking   │ nefelim4ag            │ 115w │ pending      │ pending │ cncf-cla: yes, size/L, needs-rebase      │
│               │ for rollover or s...                      │                       │      │              │         │                                          │
│ ingress-nginx │ #10912 docs: update otel documentation    │ toredash              │ 107w │ approved (1) │ pending │ cncf-cla: yes, area/docs, size/M         │
│ ingress-nginx │ #10990 Add support to make delay, size,   │ bmv126                │ 103w │ pending      │ fail    │ cncf-cla: yes, area/docs, size/L         │
│               │ burst configurabl...                      │                       │      │              │         │                                          │
│ ingress-nginx │ #11046 Acceleration update Endpoints      │ zvlb                  │ 101w │ pending      │ pending │ cncf-cla: yes, size/L, kind/feature      │
│ ingress-nginx │ #11294 Template: Distinguish paths with   │ adrianmoisey          │ 94w  │ pending      │ pending │ cncf-cla: yes, size/L, kind/bug          │
│               │ different types.                          │                       │      │              │         │                                          │
│ ingress-nginx │ #11333 Controller/Store: Retrieve         │ defaulterrr           │ 93w  │ pending      │ pending │ cncf-cla: yes, size/L, kind/feature      │
│               │ `EndpointSlices` by `Se...                │                       │      │              │         │                                          │
│ ingress-nginx │ #11490 Annotation: Make                   │ g1franc               │ 85w  │ changes (1)  │ pending │ cncf-cla: yes, size/M, kind/bug          │
│               │ `proxy-ssl-secret` optional.              │                       │      │              │         │                                          │
│ ingress-nginx │ #11655 Accept wildcard in                 │ croemmich             │ 81w  │ pending      │ pending │ cncf-cla: yes, size/S, kind/feature      │
│               │ nginx.ingress.kubernetes.io/cor...        │                       │      │              │         │                                          │
│ ingress-nginx │ #11830 Canary Weighted Consistent Hashing │ 2339478391            │ 77w  │ pending      │ pending │ cncf-cla: yes, area/docs, size/L         │
│ ingress-nginx │ #11843 TCP Proxy: Fix TLS passthrough for │ maxl99                │ 77w  │ approved (1) │ pending │ cncf-cla: yes, size/M, kind/bug          │
│               │ fragmented Clie...                        │                       │      │              │         │                                          │
│ ingress-nginx │ #11968 fix `ipallowlist` parser not       │ chengjoey             │ 73w  │ pending      │ pending │ cncf-cla: yes, size/M, needs-kind        │
│               │ handling `validation`...                  │                       │      │              │         │                                          │
│ ingress-nginx │ #12034 Fix: nginx proxy server list not   │ chengjoey             │ 71w  │ pending      │ fail    │ cncf-cla: yes, size/M, needs-rebase      │
│               │ changed                                   │                       │      │              │         │                                          │
│ ingress-nginx │ #12228 Fix make clean                     │ mneverov              │ 68w  │ pending      │ pending │ cncf-cla: yes, size/S, needs-kind        │
│ ingress-nginx │ #12256 Added label for upstream cache hit │ ajaychoudhary-hotstar │ 67w  │ pending      │ pending │ cncf-cla: yes, size/L, needs-rebase      │
│               │ status                                    │                       │      │              │         │                                          │
│ ingress-nginx │ #12384 Config/Annotations: Add            │ gavinkflam            │ 64w  │ changes (1)  │ pending │ cncf-cla: yes, area/docs, size/L         │
│               │ `ssl-forbid-http` and `for...             │                       │      │              │         │                                          │
│ ingress-nginx │ #12397 Improve shutdown logic: Wait until │ motoki317             │ 63w  │ changes (1)  │ pending │ cncf-cla: yes, size/L, kind/feature      │
│               │ no requests are...                        │                       │      │              │         │                                          │
│ ingress-nginx │ #12424 Template: Fix faulty CORS headers  │ elizabeth-dev         │ 63w  │ approved (1) │ pending │ cncf-cla: yes, size/XL, kind/bug         │
│               │ handling.                                 │                       │      │              │         │                                          │
│ ingress-nginx │ #12447 NGINX: Migrate auth cache key to   │ elizabeth-dev         │ 61w  │ approved (1) │ pending │ cncf-cla: yes, size/S, kind/feature      │
│               │ NJS.                                      │                       │      │              │         │                                          │
│ ingress-nginx │ #12448 NGINX: Migrate server redirects to │ elizabeth-dev         │ 61w  │ approved (1) │ fail    │ cncf-cla: yes, size/M, kind/feature      │
│               │ NJS.                                      │                       │      │              │         │                                          │
│ ingress-nginx │ #12450 Switch default OTel sampler to     │ GFriedrich            │ 61w  │ pending      │ pending │ cncf-cla: yes, area/docs, size/M         │
│               │ TraceIdRatioBased                         │                       │      │              │         │                                          │
│ ingress-nginx │ #12479 test(customheaders): add test for  │ qvalentin             │ 60w  │ pending      │ pending │ cncf-cla: yes, size/M, kind/bug          │
│               │ annotation added                          │                       │      │              │         │                                          │
│ ingress-nginx │ #12480 Controller: Retain default backend │ chessman              │ 60w  │ pending      │ pending │ cncf-cla: yes, size/XS, needs-ok-to-test │
│               │ service informa...                        │                       │      │              │         │                                          │
│ ingress-nginx │ #12521 Docs: Document                     │ sjlawton              │ 60w  │ changes (1)  │ pending │ cncf-cla: yes, area/docs, size/XS        │
│               │ `client-body-timeout` annotation.         │                       │      │              │         │                                          │
│ ingress-nginx │ #12626 Annotations: Allow `@` in URLs.    │ pando85               │ 57w  │ pending      │ pending │ cncf-cla: yes, size/XS, needs-ok-to-test │
│ ingress-nginx │ #12638 Improve HTTP method label handling │ jacekn                │ 57w  │ pending      │ pending │ cncf-cla: yes, size/M, needs-ok-to-test  │
│               │ in prometheus m...                        │                       │      │              │         │                                          │
│ ingress-nginx │ #12817 Allow keepalives on status port    │ rohansingh            │ 52w  │ pending      │ pending │ cncf-cla: yes, size/XS, needs-ok-to-test │
│ ingress-nginx │ #12878 Config: Do not log URL parameters. │ RichardoC             │ 50w  │ approved (1) │ pending │ cncf-cla: yes, lgtm, area/docs           │
│ ingress-nginx │ #12912 feat: Parameterize config paths.   │ emmanuel              │ 49w  │ pending      │ pending │ cncf-cla: yes, size/M, needs-ok-to-test  │
│               │ Fixes #12911.                             │                       │      │              │         │                                          │
│ ingress-nginx │ #13157 Fix kubectl plugin release         │ alexintech            │ 44w  │ pending      │ pending │ cncf-cla: yes, size/M, needs-ok-to-test  │
│ ingress-nginx │ #13264 Use PCRE on proxy redirect         │ leonardoramosantos    │ 42w  │ pending      │ pending │ cncf-cla: yes, size/S, kind/bug          │
│               │ property                                  │                       │      │              │         │                                          │
│ ingress-nginx │ #13374 Location regex should respect      │ dacohen               │ 38w  │ pending      │ fail    │ cncf-cla: yes, size/M, needs-rebase      │
│               │ Exact paths                               │                       │      │              │         │                                          │
│ ingress-nginx │ #13444 Controller: Correctly identify     │ DerekTBrown           │ 36w  │ changes (1)  │ pending │ cncf-cla: yes, area/docs, size/L         │
│               │ other pods on shutd...                    │                       │      │              │         │                                          │
│ ingress-nginx │ #13535 refactor: use slices.Contains to   │ jinjingroad           │ 33w  │ pending      │ pending │ cncf-cla: yes, size/M, needs-ok-to-test  │
│               │ simplify code                             │                       │      │              │         │                                          │
│ ingress-nginx │ #13609 Dynamic OCSP cache invalidation    │ Vexali0n              │ 30w  │ pending      │ pending │ cncf-cla: yes, size/M, needs-ok-to-test  │
╰───────────────┴───────────────────────────────────────────┴───────────────────────┴──────┴──────────────┴─────────┴──────────────────────────────────────────╯
```

