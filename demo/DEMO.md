# Giteagle Demo: Kubernetes Ecosystem

> **Generated on 2026-02-11 01:17:53 UTC**
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
╭─────────────────────────┬─────────────────────────┬────────────────┬─────────╮
│ Name                    │ Description             │ Default Branch │ Private │
├─────────────────────────┼─────────────────────────┼────────────────┼─────────┤
│ kubernetes              │ Production-Grade        │ master         │ No      │
│                         │ Container Scheduling    │                │         │
│                         │ and Manageme...         │                │         │
│ website                 │ Kubernetes website and  │ main           │ No      │
│                         │ documentation repo:     │                │         │
│ release                 │ Release infrastructure  │ master         │ No      │
│                         │ for Kubernetes and      │                │         │
│                         │ related ...             │                │         │
│ minikube                │ Run Kubernetes locally  │ master         │ No      │
│ test-infra              │ Test infrastructure for │ master         │ No      │
│                         │ the Kubernetes project. │                │         │
│ enhancements            │ Enhancements tracking   │ master         │ No      │
│                         │ repo for Kubernetes     │                │         │
│ community               │ Kubernetes community    │ master         │ No      │
│                         │ content                 │                │         │
│ kube-state-metrics      │ Add-on agent to         │ main           │ No      │
│                         │ generate and expose     │                │         │
│                         │ cluster-level ...       │                │         │
│ node-problem-detector   │ This is a place for     │ master         │ No      │
│                         │ various problem         │                │         │
│                         │ detectors runn...       │                │         │
│ kompose                 │ Convert Compose to      │ main           │ No      │
│                         │ Kubernetes              │                │         │
│ kops                    │ Kubernetes Operations   │ master         │ No      │
│                         │ (kOps) - Production     │                │         │
│                         │ Grade k8...             │                │         │
│ kubernetes-template-pr… │ A template for starting │ main           │ No      │
│                         │ new projects on the     │                │         │
│                         │ github...               │                │         │
│ git-sync                │ A sidecar app which     │ master         │ No      │
│                         │ clones a git repo and   │                │         │
│                         │ keeps it...             │                │         │
│ k8s.io                  │ Code and configuration  │ main           │ No      │
│                         │ to manage Kubernetes    │                │         │
│                         │ projec...               │                │         │
│ client-go               │ Go client for           │ master         │ No      │
│                         │ Kubernetes.             │                │         │
│ gengo                   │ gengo library for code  │ master         │ No      │
│                         │ generation.             │                │         │
│ perf-tests              │ Performance tests and   │ master         │ No      │
│                         │ benchmarks              │                │         │
│ ingress-nginx           │ Ingress NGINX           │ main           │ No      │
│                         │ Controller for          │                │         │
│                         │ Kubernetes              │                │         │
│ kubeadm                 │ Aggregator for issues   │ main           │ No      │
│                         │ filed against kubeadm   │                │         │
│ repo-infra              │ Kubernetes repository   │ master         │ No      │
│                         │ infrastucture tools     │                │         │
│ dns                     │ Kubernetes DNS service  │ master         │ No      │
│ apimachinery            │                         │ master         │ No      │
│ apiserver               │ Library for writing a   │ master         │ No      │
│                         │ Kubernetes-style API    │                │         │
│                         │ server.                 │                │         │
│ sample-apiserver        │ Reference               │ master         │ No      │
│                         │ implementation of an    │                │         │
│                         │ apiserver for a cus...  │                │         │
│ kube-aggregator         │ Aggregator for          │ master         │ No      │
│                         │ Kubernetes-style API    │                │         │
│                         │ servers: dynam...       │                │         │
│ metrics                 │ Kubernetes              │ master         │ No      │
│                         │ metrics-related API     │                │         │
│                         │ types and clients       │                │         │
│ kubectl                 │ Issue tracker and       │ master         │ No      │
│                         │ mirror of kubectl code  │                │         │
│ autoscaler              │ Autoscaling components  │ master         │ No      │
│                         │ for Kubernetes          │                │         │
│ examples                │ Kubernetes application  │ master         │ No      │
│                         │ example tutorials       │                │         │
│ api                     │ The canonical location  │ master         │ No      │
│                         │ of the Kubernetes API   │                │         │
│                         │ defin...                │                │         │
│ apiextensions-apiserver │ API server for API      │ master         │ No      │
│                         │ extensions like         │                │         │
│                         │ CustomResourceD...      │                │         │
│ utils                   │ Non-Kubernetes-specific │ master         │ No      │
│                         │ utility libraries which │                │         │
│                         │ ar...                   │                │         │
│ kube-openapi            │ Kubernetes OpenAPI spec │ master         │ No      │
│                         │ generation & serving    │                │         │
│ sig-release             │ Repo for SIG release    │ master         │ No      │
│ code-generator          │ Generators for          │ master         │ No      │
│                         │ kube-like API types     │                │         │
│ steering                │ The Kubernetes Steering │ main           │ No      │
│                         │ Committee               │                │         │
│ ingress-gce             │ Ingress controller for  │ master         │ No      │
│                         │ Google Cloud            │                │         │
│ sample-controller       │ Repository for sample   │ master         │ No      │
│                         │ controller. Complements │                │         │
│                         │ samp...                 │                │         │
│ publishing-bot          │ Code behind the robot   │ master         │ No      │
│                         │ to publish from staging │                │         │
│                         │ to r...                 │                │         │
│ cloud-provider-aws      │ Cloud provider for AWS  │ master         │ No      │
│ cloud-provider-opensta… │                         │ master         │ No      │
│ cloud-provider-gcp      │ cloud-provider-gcp      │ master         │ No      │
│                         │ contains several        │                │         │
│                         │ projects used ...       │                │         │
│ cloud-provider-vsphere  │ Kubernetes Cloud        │ master         │ No      │
│                         │ Provider for vSphere    │                │         │
│                         │ https://clou...         │                │         │
│ org                     │ Meta configuration for  │ main           │ No      │
│                         │ Kubernetes Github Org   │                │         │
│ contributor-site        │ Code for kubernetes.dev │ master         │ No      │
│ kube-controller-manager │ kube-controller-manager │ master         │ No      │
│                         │ component configs       │                │         │
│ kube-scheduler          │ kube-scheduler          │ master         │ No      │
│                         │ component configs       │                │         │
│ kubelet                 │ kubelet component       │ master         │ No      │
│                         │ configs                 │                │         │
│ kube-proxy              │ kube-proxy component    │ master         │ No      │
│                         │ configs                 │                │         │
│ cli-runtime             │ Set of helpers for      │ master         │ No      │
│                         │ creating kubectl        │                │         │
│                         │ commands and p...       │                │         │
│ sample-cli-plugin       │ Sample kubectl plugin   │ master         │ No      │
│ cloud-provider-alibaba… │ CloudProvider for       │ master         │ No      │
│                         │ Alibaba Cloud           │                │         │
│ cluster-bootstrap       │                         │ master         │ No      │
│ cloud-provider          │ cloud-provider defines  │ master         │ No      │
│                         │ the shared interfaces   │                │         │
│                         │ which...                │                │         │
│ klog                    │ Leveled execution logs  │ main           │ No      │
│                         │ for Go (fork of         │                │         │
│                         │ https://git...          │                │         │
│ node-api                │                         │ master         │ No      │
│ cloud-provider-sample   │ Sample of how to build  │ master         │ No      │
│                         │ a cloud provider repo.  │                │         │
│                         │ This...                 │                │         │
│ component-base          │ Shared code for         │ master         │ No      │
│                         │ kubernetes core         │                │         │
│                         │ components              │                │         │
│ csi-translation-lib     │ Staging repo for CSI    │ master         │ No      │
│                         │ Migration/Translation   │                │         │
│                         │ librari...              │                │         │
│ committee-security-res… │ Kubernetes Security     │ main           │ No      │
│                         │ Process and Security    │                │         │
│                         │ Committee...            │                │         │
│ cri-api                 │ Container Runtime       │ master         │ No      │
│                         │ Interface (CRI) – a     │                │         │
│                         │ plugin inter...         │                │         │
│ legacy-cloud-providers  │ This repository hosts   │ master         │ No      │
│                         │ the legacy in-tree      │                │         │
│                         │ cloud pro...            │                │         │
│ system-validators       │ A set of                │ main           │ No      │
│                         │ system-oriented         │                │         │
│                         │ validators for kubeadm  │                │         │
│                         │ pr...                   │                │         │
│ controller-manager      │ This repo is intended   │ master         │ No      │
│                         │ to contain common       │                │         │
│                         │ public lib...           │                │         │
│ mount-utils             │ Package mount defines   │ master         │ No      │
│                         │ an interface to         │                │         │
│                         │ mounting fil...         │                │         │
│ .github                 │ Default files for all   │ master         │ No      │
│                         │ repos in the Kubernetes │                │         │
│                         │ GitH...                 │                │         │
│ component-helpers       │ High-level helpers for  │ master         │ No      │
│                         │ Kubernetes components   │                │         │
│ sig-testing             │ Home for SIG Testing    │ master         │ No      │
│                         │ discussion and          │                │         │
│                         │ documents.              │                │         │
│ pod-security-admission  │ Kubernetes Pod Security │ master         │ No      │
│                         │ Standards               │                │         │
│                         │ implementation -...     │                │         │
│ sig-security            │ Process documentation,  │ main           │ No      │
│                         │ non-code deliverables,  │                │         │
│                         │ and ...                 │                │         │
│ design-proposals-archi… │ Archive of Kubernetes   │ main           │ No      │
│                         │ Design Proposals        │                │         │
│ registry.k8s.io         │ This project is the     │ main           │ No      │
│                         │ repo for                │                │         │
│                         │ registry.k8s.io, the    │                │         │
│                         │ ...                     │                │         │
│ kms                     │ Kubernetes KMS          │ master         │ No      │
│                         │ implementation          │                │         │
│ dynamic-resource-alloc… │                         │ master         │ No      │
│ cel-admission-webhook   │                         │ main           │ No      │
│ endpointslice           │                         │ master         │ No      │
│ cri-client              │ Container Runtime       │ master         │ No      │
│                         │ Interface client        │                │         │
│                         │ implementation          │                │         │
│ externaljwt             │ Synced from             │ master         │ No      │
│                         │ kubernetes/kubernetes/… │                │         │
╰─────────────────────────┴─────────────────────────┴────────────────┴─────────╯

Total: 78 repositories
```


## 3. Recent Activity on kubernetes/kubernetes

Show the 15 most recent activities (commits, pull requests, issues) from the core Kubernetes repository over the last 7 days.

```bash
$ uv run giteagle activity kubernetes/kubernetes --days 7 --limit 15
```

```
╭───────────────────────────────── Repository ─────────────────────────────────╮
│ kubernetes/kubernetes                                                        │
│ Production-Grade Container Scheduling and Management                         │
╰──────────────────────────────────────────────────────────────────────────────╯
                             Activity (last 7 days)                             
╭──────────────┬────────────────────────┬───────────────────┬──────────────────╮
│ Type         │ Title                  │ Author            │ Date             │
├──────────────┼────────────────────────┼───────────────────┼──────────────────┤
│ pull_request │ WIP: move go-runner    │ BenTheElder       │ 2026-02-11 00:59 │
│              │ back to kubernetes     │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-11 00:42 │
│              │ #135675 from           │                   │                  │
│              │ richabanker/merged-di… │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-11 00:41 │
│              │ #135395 from           │                   │                  │
│              │ pohly/apimachinery-wa… │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-10 23:47 │
│              │ #135256 from           │                   │                  │
│              │ natasha41575/pod-gen-… │                   │                  │
│ pull_request │ add dockerized go      │ BenTheElder       │ 2026-02-10 22:58 │
│              │ cache chmod to  `make  │                   │                  │
│              │ clean`                 │                   │                  │
│ pull_request │ Pipe feature gate of   │ michaelasp        │ 2026-02-10 22:35 │
│              │ unlockWhileProcessing  │                   │                  │
│ pull_request │ Promote                │ troychiu          │ 2026-02-10 22:10 │
│              │ DRAPrioritizedList to  │                   │                  │
│              │ GA                     │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-10 21:30 │
│              │ #136716 from           │                   │                  │
│              │ yonizxz/concurrent-no… │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-10 21:30 │
│              │ #134981 from           │                   │                  │
│              │ haircommander/drop-cp… │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-10 19:54 │
│              │ #136911 from           │                   │                  │
│              │ pohly/dra-e2e-data-ra… │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-10 19:54 │
│              │ #136734 from           │                   │                  │
│              │ sunya-ch/sunya-ch/fix… │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-10 18:38 │
│              │ #136826 from           │                   │                  │
│              │ alvaroaleman/bumpv0.32 │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-10 18:38 │
│              │ #136339 from           │                   │                  │
│              │ ffromani/deprecate-cu… │                   │                  │
│ pull_request │ test: fix the flaking  │ shwetha-s-poojary │ 2026-02-10 14:02 │
│              │ TestWebhookConversion… │                   │                  │
│ commit       │ CHANGELOG: Update      │ k8s-release-robot │ 2026-02-10 13:06 │
│              │ directory for v1.32.12 │                   │                  │
│              │ release                │                   │                  │
╰──────────────┴────────────────────────┴───────────────────┴──────────────────╯

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
Fetched 65 activities from kubernetes/ingress-nginx
╭─────────────────────────── Summary (last 7 days) ────────────────────────────╮
│ Total Activities: 190                                                        │
│ Repositories: 3                                                              │
│ Contributors: 56                                                             │
╰──────────────────────────────────────────────────────────────────────────────╯
    By Activity Type    
                        
  Type           Count  
 ────────────────────── 
  pull_request      92  
  commit            59  
  issue             39  
                        
             Top Contributors              
                                           
  Username                     Activities  
 ───────────────────────────────────────── 
  k8s-ci-robot                         29  
  everettraven                         27  
  Gacko                                22  
  k8s-infra-cherrypick-robot           17  
  minikube-bot                         14  
                                           
              By Repository              
                                         
  Repository                 Activities  
 ─────────────────────────────────────── 
  kubernetes/kubernetes             100  
  kubernetes/ingress-nginx           59  
  kubernetes/minikube                31  
                                         
```


## 5. Activity Timeline

Visualize weekly activity over the past 30 days across three Kubernetes repositories.

```bash
$ uv run giteagle timeline kubernetes/kubernetes kubernetes/minikube kubernetes/ingress-nginx --days 30 --granularity week
```

```
╭──────────────────────────────────────────────────────────────────────────────╮
│ Activity Timeline (weekly)                                                   │
╰──────────────────────────────────────────────────────────────────────────────╯
2026-01-12: █████████████████████████ 228
2026-01-19: ███████████████████ 176
2026-01-26: ██████████████████████████████ 269
2026-02-02: ████████████████████████████████████████ 355
2026-02-09: ██████████████████ 167
```


## 6. Unified Git Log Across Repos

Browse commits across multiple repositories in a single unified view, like `tig` but for multiple repos. Each repo gets a distinct color, commits are grouped by date, and merge commits are marked.

```bash
$ uv run giteagle log kubernetes/kubernetes kubernetes/minikube kubernetes/ingress-nginx --days 3 --limit 15
```

```
Fetched 10 commits from kubernetes/kubernetes
Fetched 1 commits from kubernetes/minikube
Fetched 4 commits from kubernetes/ingress-nginx
 ● 2026-02-11  kubernetes     46ac9df  Merge pull request #135675 from 
richabanker/merged-discovery (merge)
 │             kubernetes     eb09a3c  Merge pull request #135395 from 
pohly/apimachinery-wait-for-cache-sync (merge)
 ● 2026-02-10  kubernetes     99d4b4d  Merge pull request #135256 from 
natasha41575/pod-gen-field (merge)
 │             kubernetes     870e292  Merge pull request #136716 from 
yonizxz/concurrent-node-syncs-split (merge)
 │             kubernetes     c9534cb  Merge pull request #134981 from 
haircommander/drop-cpu-load (merge)
 │             kubernetes     3e15c6f  Merge pull request #136911 from 
pohly/dra-e2e-data-race (merge)
 │             kubernetes     1bb2e12  Merge pull request #136734 from 
sunya-ch/sunya-ch/fix-gather-shared-id (merge)
 │             minikube       f750803  Build(deps): Bump the golang-org group 
with 6 updates (#22647)
 │             kubernetes     65f09e6  Merge pull request #136826 from 
alvaroaleman/bumpv0.32 (merge)
 │             kubernetes     e7f26c6  Merge pull request #136339 from 
ffromani/deprecate-customcpucfsquota-fg-not-feature (merge)
 │             kubernetes     f425715  CHANGELOG: Update directory for v1.32.12 
release
 │             ingress-nginx  efcd54f  Controller: Enable SSL Passthrough when 
requested on before HTTP-only hosts. (#14555)
 ● 2026-02-09  ingress-nginx  72d99b3  CI: Update Helm to v4.1.1. (#14552)
 │             ingress-nginx  a2341e5  Bump github/codeql-action from 4.32.0 to 
4.32.2 in the actions group (#14544)
 │             ingress-nginx  ded3b60  Annotations: Use dedicated regular 
expression for `proxy-cookie-domain`. (#14536)

Total: 15 commits across 3 repositories
```


Filter to a specific contributor:

```bash
$ uv run giteagle log kubernetes/kubernetes kubernetes/minikube --author k8s-ci-robot --days 3
```

```
Fetched 43 commits from kubernetes/kubernetes
Fetched 1 commits from kubernetes/minikube
 ● 2026-02-11  kubernetes  46ac9df  Merge pull request #135675 from 
richabanker/merged-discovery (merge)
 │             kubernetes  eb09a3c  Merge pull request #135395 from 
pohly/apimachinery-wait-for-cache-sync (merge)
 ● 2026-02-10  kubernetes  99d4b4d  Merge pull request #135256 from 
natasha41575/pod-gen-field (merge)
 │             kubernetes  870e292  Merge pull request #136716 from 
yonizxz/concurrent-node-syncs-split (merge)
 │             kubernetes  c9534cb  Merge pull request #134981 from 
haircommander/drop-cpu-load (merge)
 │             kubernetes  3e15c6f  Merge pull request #136911 from 
pohly/dra-e2e-data-race (merge)
 │             kubernetes  1bb2e12  Merge pull request #136734 from 
sunya-ch/sunya-ch/fix-gather-shared-id (merge)
 │             kubernetes  65f09e6  Merge pull request #136826 from 
alvaroaleman/bumpv0.32 (merge)
 │             kubernetes  e7f26c6  Merge pull request #136339 from 
ffromani/deprecate-customcpucfsquota-fg-not-feature (merge)
 │             kubernetes  7f890ab  Merge pull request #136802 from 
pohly/fix-data-race-refs-populaterefs (merge)
 │             kubernetes  2a9b8ba  Merge pull request #136787 from 
ahmedtd/bump-ctb (merge)
 │             kubernetes  01b283a  Merge pull request #136907 from 
aojea/ipaddress_flake (merge)
 │             kubernetes  59cdded  Merge pull request #136901 from 
Phaow/vac-fix (merge)
 │             kubernetes  4670994  Merge pull request #136898 from 
carlory/kubeadm-ContainerRuntimeVersion-1-37 (merge)
 │             kubernetes  76b4a90  Merge pull request #136326 from 
bart0sh/PR218-migrate-kubelet_node_status-to-contextual-logging (merge)
 │             kubernetes  65b1000  Merge pull request #135749 from 
novahe/fix-defer-latency (merge)
 │             kubernetes  44dc4cb  Merge pull request #136888 from 
neolit123/revert-136130-kubeadm_use_newclientset (merge)
 │             kubernetes  b6f27f1  Merge pull request #136856 from 
pohly/dra-integration-timeouts (merge)
 │             kubernetes  0bb7533  Merge pull request #135464 from 
MikeSpreitzer/better-concurrency-test-margin (merge)
 │             kubernetes  1955210  Merge pull request #134044 from 
mcallzbl/master (merge)
 │             kubernetes  7b0310a  Merge pull request #136820 from 
dims/update-otel-deps (merge)
 │             kubernetes  f693c45  Merge pull request #136775 from 
atombrella/feature/activate_modernize_slicessort (merge)
 ● 2026-02-09  kubernetes  fc74562  Merge pull request #136808 from 
nmn3m/kubelet-contextual-logging (merge)
 │             kubernetes  09e1c9f  Merge pull request #136455 from 
pohly/client-go-simpleclient-undeprecation (merge)
 │             kubernetes  139e78d  Merge pull request #136337 from 
pohly/dra-e2e-hostpath-image-selection (merge)
 │             kubernetes  e73221c  Merge pull request #136488 from 
thockin/fix_bad_arg_name_in_dv (merge)
 │             kubernetes  a39c820  Merge pull request #136423 from 
neolit123/1.36-remove-flex-volume-support-from-kubeadm (merge)
 │             kubernetes  97a2334  Merge pull request #136778 from 
Jefftree/etcd-metrics-typo (merge)
 ● 2026-02-08  kubernetes  918b5ac  Merge pull request #136840 from 
atombrella/feature/fmt_sprintf_unneeded (merge)

Total: 29 commits across 1 repositories
```


## 7. Daily Standup Report

Generate a standup-ready summary of recent activity across repositories. The `standup` command groups activities by repo and categorizes them as commits, PRs opened/merged/closed, and issues. It auto-detects the authenticated user when a GitHub token is set.

```bash
$ uv run giteagle standup kubernetes/kubernetes kubernetes/ingress-nginx --days 3
```

```
Fetched 200 activities from kubernetes/kubernetes
Fetched 34 activities from kubernetes/ingress-nginx
No activity for igormilovanovic since 2026-02-08
```


## 8. Cross-Repo PR Dashboard

Show all open pull requests across repos with review status, CI status, age, and labels. PRs older than `--stale` days are highlighted as stale.

```bash
$ uv run giteagle prs kubernetes/kubernetes kubernetes/ingress-nginx --stale 7
```

```
Fetched 100 open PRs from kubernetes/kubernetes
Fetched 44 open PRs from kubernetes/ingress-nginx
                            Open Pull Requests (144)                            
╭───────────────┬───┬───────────────────────┬──────┬──────────────┬─────────┬──╮
│ Repo          │ … │ Author                │ Age  │ Reviews      │ CI      │  │
├───────────────┼───┼───────────────────────┼──────┼──────────────┼─────────┼──┤
│ kubernetes    │ … │ shawnhanx             │ 254w │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ shawnhanx             │ 234w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ shawnhanx             │ 228w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ shawnhanx             │ 228w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ shawnhanx             │ 226w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ tomaspinho            │ 203w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ aslafy-z              │ 202w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ chrisshino            │ 195w │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ + │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ alowde                │ 179w │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ kirs                  │ 171w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ hassenius             │ 157w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ HirazawaUi            │ 148w │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ ghostloda             │ 142w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ skitt                 │ 140w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ Spazzy757             │ 139w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ chotiwat              │ 123w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ machine424            │ 120w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ travisghansen         │ 118w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ 2 │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ skitt                 │ 117w │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ skitt                 │ 116w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ nefelim4ag            │ 115w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ DaGenix               │ 114w │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ omertuc               │ 112w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ toredash              │ 106w │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ barrykp               │ 105w │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ bmv126                │ 103w │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ PascalBourdier        │ 103w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ a │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ zvlb                  │ 101w │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ msvticket             │ 96w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ adrianmoisey          │ 94w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ defaulterrr           │ 93w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ towca                 │ 91w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ a │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ nmreadelf             │ 90w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ SOF3                  │ 87w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ g1franc               │ 85w  │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ gjkim42               │ 85w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ huutomerkki           │ 83w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ antomy-gc             │ 83w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ LionelJouin           │ 82w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ HirazawaUi            │ 82w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ linxiulei             │ 82w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ croemmich             │ 81w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ Ritikaa96             │ 79w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ BenTheElder           │ 79w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ 2339478391            │ 77w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ maxl99                │ 76w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ tlwr                  │ 75w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ hshiina               │ 74w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ hshiina               │ 74w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ vrutkovs              │ 73w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ chengjoey             │ 73w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ dsyer                 │ 72w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ JanSchep              │ 72w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ chengjoey             │ 71w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ huochexizhan          │ 71w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ linxiulei             │ 70w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ mneverov              │ 67w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ ajaychoudhary-hotstar │ 67w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ knrc                  │ 66w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ knrc                  │ 66w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ rexagod               │ 66w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ vrutkovs              │ 65w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ tkashem               │ 65w  │ approved (2) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ ffromani              │ 65w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ gavinkflam            │ 64w  │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ VannTen               │ 64w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ acumino               │ 63w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ motoki317             │ 63w  │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ bouaouda-achraf       │ 63w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ elizabeth-dev         │ 62w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ Tal-or                │ 61w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ badouralix            │ 61w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ pohly                 │ 61w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ + │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ elizabeth-dev         │ 61w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ elizabeth-dev         │ 61w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ GFriedrich            │ 61w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ pohly                 │ 61w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ tkashem               │ 61w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ a │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ qvalentin             │ 60w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ chessman              │ 60w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ sjlawton              │ 59w  │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ xyz-li                │ 59w  │ approved (3) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ pohly                 │ 59w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ + │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ pohly                 │ 59w  │ changes (1)  │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ pohly                 │ 59w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ HirazawaUi            │ 59w  │ pending      │ pending │  │
│               │ : │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ SuperQ                │ 58w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ pando85               │ 57w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ jacekn                │ 57w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ esotsal               │ 55w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ carlory               │ 54w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ adriancuadrado        │ 54w  │ approved (2) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ vaibhav2107           │ 54w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ jm-franc              │ 54w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ zylxjtu               │ 53w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ AwesomePatrol         │ 52w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ rohansingh            │ 52w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ mochizuki875          │ 51w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ novahe                │ 51w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ a │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ lentzi90              │ 51w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ bart0sh               │ 51w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ yue9944882            │ 51w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ oliverguenther        │ 50w  │ changes (1)  │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ laozc                 │ 50w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ RichardoC             │ 50w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ davidxia              │ 50w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ atiratree             │ 50w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ emmanuel              │ 49w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ vrutkovs              │ 49w  │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ ania-borowiec         │ 49w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ cbandy                │ 48w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ HirazawaUi            │ 47w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ iPraveenParihar       │ 46w  │ approved (2) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ HirazawaUi            │ 46w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ aiburegit             │ 45w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ sgaist                │ 45w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ alexintech            │ 44w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ yude                  │ 44w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ ntnn                  │ 43w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ fasaxc                │ 43w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ HirazawaUi            │ 43w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ HirazawaUi            │ 43w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ mbergo                │ 42w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ xigang                │ 42w  │ approved (2) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ leonardoramosantos    │ 41w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ pravk03               │ 41w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ carlory               │ 40w  │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ rexagod               │ 40w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ jaehanbyun            │ 40w  │ approved (2) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ carlory               │ 39w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ ArangoGutierrez       │ 39w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ Chunxia202410         │ 38w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ dacohen               │ 38w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ yangjunmyfm192085     │ 38w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ shadowofs             │ 38w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ alimaazamat           │ 37w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ aryasoni98            │ 37w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ Chunxia202410         │ 37w  │ approved (1) │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ sreeram-venkitesh     │ 37w  │ pending      │ fail    │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ condaatje             │ 36w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ DerekTBrown           │ 36w  │ changes (1)  │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ kubernetes    │ … │ utam0k                │ 36w  │ approved (1) │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ jinjingroad           │ 33w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│ ingress-nginx │ … │ Vexali0n              │ 30w  │ pending      │ pending │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
│               │ … │                       │      │              │         │  │
╰───────────────┴───┴───────────────────────┴──────┴──────────────┴─────────┴──╯
```


## 9. DORA-Style PR Metrics

Track engineering velocity with DORA-inspired metrics: median time-to-merge (TTM), median time-to-first-review (TTFR), merge rate, and PR throughput per week. Includes trend comparison (up/down/stable) vs the previous period.

```bash
$ uv run giteagle stats kubernetes/kubernetes kubernetes/ingress-nginx --days 30
```

```
Warning: Failed to fetch kubernetes/kubernetes: HTTP 500
Fetched 198 closed PRs from kubernetes/ingress-nginx
                           PR Metrics (last 30 days)                           
╭───────────────┬────────┬────────────┬─────────────┬────────────┬────────────╮
│ Repo          │ Merged │ Median TTM │ Median TTFR │ Merge Rate │ PRs/week   │
├───────────────┼────────┼────────────┼─────────────┼────────────┼────────────┤
│ ingress-nginx │    169 │ 1h 5m      │ 11m         │        93% │ 39.4  ^ up │
╰───────────────┴────────┴────────────┴─────────────┴────────────┴────────────╯
```

---

*Demo completed at 2026-02-11 01:19:11 UTC.*
*Run with giteagle, version 0.1.0.*
