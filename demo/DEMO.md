# Giteagle Demo: Kubernetes Ecosystem

> **Generated on 2026-02-08 23:00:08 UTC**
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
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-08 19:23 │
│              │ #136840 from           │                   │                  │
│              │ atombrella/feature/fm… │                   │                  │
│ issue        │ govulncheck fails with │ Pnkcaht           │ 2026-02-08 19:18 │
│              │ internal errors when   │                   │                  │
│              │ run against Kube...    │                   │                  │
│ pull_request │ Remove unneeded use of │ atombrella        │ 2026-02-08 13:35 │
│              │ fmt.Sprintf in         │                   │                  │
│              │ test/{integration,e2e} │                   │                  │
│ commit       │ Remove unneeded use of │ atombrella        │ 2026-02-08 13:34 │
│              │ fmt.Sprintf in         │                   │                  │
│              │ test/{integration,e2e} │                   │                  │
│ pull_request │ kubectl create: mark   │ Mujib-Ahasan      │ 2026-02-07 21:43 │
│              │ --edit flag as         │                   │                  │
│              │ deprecated             │                   │                  │
│ pull_request │ Enable declarative     │ darshansreenivas  │ 2026-02-07 20:42 │
│              │ validation for apps    │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-07 16:43 │
│              │ #136767 from           │                   │                  │
│              │ Sahil-4555/atomic-typ… │                   │                  │
│ pull_request │ Update OpenTelemetry   │ dims              │ 2026-02-07 14:22 │
│              │ dependencies to latest │                   │                  │
│              │ versions               │                   │                  │
│ pull_request │ Update go-openapi      │ dims              │ 2026-02-07 13:11 │
│              │ dependencies           │                   │                  │
│              │ (jsonpointer,          │                   │                  │
│              │ jsonreference, ...     │                   │                  │
│ pull_request │ Improve Job validation │ kairosci          │ 2026-02-07 12:55 │
│              │ error message for      │                   │                  │
│              │ startTime              │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-07 01:00 │
│              │ #135335 from           │                   │                  │
│              │ carlory/cleanup        │                   │                  │
│ commit       │ Merge pull request     │ k8s-ci-robot      │ 2026-02-06 22:36 │
│              │ #136621 from           │                   │                  │
│              │ ermias19/fix-validati… │                   │                  │
│ pull_request │ Validation-gen:        │ itzPranshul       │ 2026-02-06 20:37 │
│              │ migrate                │                   │                  │
│              │ ControllerRevision.Da… │                   │                  │
│              │ to declarati...        │                   │                  │
│ commit       │ feat(wait): introduce  │ AustinAbro321     │ 2026-02-06 20:10 │
│              │ waitOptions.RunWaitCo… │                   │                  │
│              │ (#136781)              │                   │                  │
│ commit       │ CHANGELOG: Update      │ k8s-release-robot │ 2026-02-06 19:12 │
│              │ directory for          │                   │                  │
│              │ v1.36.0-alpha.1        │                   │                  │
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
Fetched 94 activities from kubernetes/minikube
Fetched 78 activities from kubernetes/ingress-nginx
╭─────────────────────────── Summary (last 7 days) ────────────────────────────╮
│ Total Activities: 218                                                        │
│ Repositories: 3                                                              │
│ Contributors: 62                                                             │
╰──────────────────────────────────────────────────────────────────────────────╯
    By Activity Type    
                        
  Type           Count  
 ────────────────────── 
  pull_request     120  
  commit            77  
  issue             21  
                        
      Top Contributors       
                             
  Username       Activities  
 ─────────────────────────── 
  Gacko                  45  
  k8s-ci-robot           28  
  minikube-bot           20  
  medyagh                18  
  dependabot             18  
                             
              By Repository              
                                         
  Repository                 Activities  
 ─────────────────────────────────────── 
  kubernetes/kubernetes             100  
  kubernetes/ingress-nginx           67  
  kubernetes/minikube                51  
                                         
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
2026-01-05: ███ 32
2026-01-12: ████████████████████████ 229
2026-01-19: ████████████████████ 194
2026-01-26: ████████████████████████████████████ 352
2026-02-02: ████████████████████████████████████████ 381
```

---

*Demo completed at 2026-02-08 23:00:43 UTC.*
*Run with giteagle, version 0.1.0.*
