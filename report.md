# API Reliability Monitor — SLA Report

> Last updated: **2026-07-05 21:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.6% | 2235.5 | 10206.7 | 1000ms | 267/1309 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 123.4 | 4595.4 | 1500ms | 4/1309 |
| ❌ | `nasa_apod` | 73.95% | 49.5% | 3389.4 | 11152.5 | 2000ms | 661/1309 |
| ❌ | `ipapi_check` | 76.62% | 99.92% | 154.9 | 4507.0 | 2500ms | 1/1309 |
| ⚠️ | `dog_ceo_random` | 96.26% | 96.79% | 531.4 | 10244.1 | 2500ms | 42/1309 |
| ⚠️ | `open_meteo_weather` | 98.62% | 96.87% | 735.9 | 14877.1 | 2000ms | 41/1309 |
| ⚠️ | `rest_countries` | 98.85% | 98.55% | 319.6 | 10221.5 | 2500ms | 19/1309 |
| ✅ | `useless_fact` | 99.62% | 99.69% | 632.7 | 10229.6 | 2500ms | 4/1309 |
| ✅ | `catfact_random` | 99.77% | 99.31% | 255.9 | 10080.2 | 3000ms | 9/1309 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 97.9 | 4328.4 | 1500ms | 1/1309 |
| ✅ | `agify_name` | 99.92% | 99.69% | 384.3 | 16112.2 | 2000ms | 4/1309 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 213.6 | 3882.8 | 2000ms | 2/1309 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4477.1 | 65.71% |
| `nasa_apod` | 01:00 | 4324.4 | 62.16% |
| `nasa_apod` | 09:00 | 4282.5 | 55.36% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `nasa_apod` | 18:00 | 3840.1 | 54.41% |
| `nasa_apod` | 11:00 | 3686.0 | 53.52% |
| `nasa_apod` | 20:00 | 3626.6 | 50.6% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
