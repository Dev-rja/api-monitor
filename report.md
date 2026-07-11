# API Reliability Monitor — SLA Report

> Last updated: **2026-07-11 11:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.53% | 2145.4 | 10206.7 | 1000ms | 267/1371 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.5 | 4595.4 | 1500ms | 4/1371 |
| ❌ | `nasa_apod` | 74.84% | 50.47% | 3299.2 | 11152.5 | 2000ms | 679/1371 |
| ❌ | `ipapi_check` | 75.64% | 99.93% | 154.5 | 4507.0 | 2500ms | 1/1371 |
| ❌ | `dog_ceo_random` | 94.89% | 96.79% | 528.0 | 10244.1 | 2500ms | 44/1371 |
| ⚠️ | `open_meteo_weather` | 98.61% | 97.01% | 728.9 | 14877.1 | 2000ms | 41/1371 |
| ⚠️ | `rest_countries` | 98.91% | 98.61% | 314.6 | 10221.5 | 2500ms | 19/1371 |
| ✅ | `useless_fact` | 99.64% | 99.71% | 633.9 | 10229.6 | 2500ms | 4/1371 |
| ✅ | `catfact_random` | 99.78% | 99.34% | 255.7 | 10080.2 | 3000ms | 9/1371 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.9 | 4328.4 | 1500ms | 1/1371 |
| ✅ | `agify_name` | 99.93% | 99.71% | 384.8 | 16112.2 | 2000ms | 4/1371 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 210.9 | 3882.8 | 2000ms | 2/1371 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 09:00 | 4088.2 | 52.54% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4018.9 | 54.93% |
| `nasa_apod` | 01:00 | 3943.4 | 56.1% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 18:00 | 3749.8 | 52.78% |
| `nasa_apod` | 12:00 | 3546.1 | 53.33% |
| `nasa_apod` | 11:00 | 3530.4 | 52.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
